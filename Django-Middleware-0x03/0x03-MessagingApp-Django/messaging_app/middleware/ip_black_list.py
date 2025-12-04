from django.http import HttpResponseForbidden
from django.conf import settings
class Ipblacklistmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        if hasattr(settings, 'Banned_IPs'):
            banned_ips = settings.Banned_IPs
            ip = request.META.get('REMOTE_ADDR')
            if ip in banned_ips:
                return HttpResponseForbidden("Your IP is banned.")
        response = self.get_response(request)
        return response
# messaging_app/middleware/ip_black_list.py