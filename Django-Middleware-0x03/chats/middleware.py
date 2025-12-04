import time
import logging
from django.http import JsonResponse
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta
from django.shortcuts import HttpResponse,request



class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start_time =time.time()
        method = request.method
        path = request.get_full_path()
        with open("requests.log ", 'a') as  log_file:
            log_file.write(f"{method} {path} {start_time}\n")  # Write to log file
        response = self.get_response(request)
        return response


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.LIMIT = 5
        self.window = 60  # seconds
        self.block = 300  # seconds if user exceds the limit will be blocked for 5 minutes for sending messages
        self.get_response = get_response
    
    def __call__(self, request):
        ip= self.get_client_ip(request)
        if request.method == 'POST':
            count_key = f"ip_send_msg{ip}"
            blocked =f"blocked_msg{ip}"
            if cache.get(blocked):
                return JsonResponse({"detail": "You are temporarily blocked from sending messages due to excessive usage."}, status=429)    
            count = cache.get(count_key, 0)
            if count == 0:
                cache.set(count_key, 1, timeout=self.window)
            else:
                cache.inc(count_key)
            if count > self.LIMIT:
                cache.set(blocked, True, timeout=self.block)
                return JsonResponse({"Error": 
                    "Message Limit exceeded. You are blocked"}, status=429)
        return self.get_response(request)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")
        
                
                
            