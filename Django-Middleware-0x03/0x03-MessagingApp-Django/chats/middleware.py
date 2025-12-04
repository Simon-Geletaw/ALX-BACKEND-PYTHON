import time


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
    