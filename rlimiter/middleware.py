from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.urls import reverse

from main.rate_limiter import RateLimitingService
from main.models import *

class RateLimitingMiddleware(MiddlewareMixin):
    def get_client_ip_address(request):
        req_headers = request.META
        x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for_value:
            ip_addr = x_forwarded_for_value.split(',')[-1].strip()
        else:
            ip_addr = req_headers.get('REMOTE_ADDR')
        return ip_addr

    def map_raw_request(request):
        ip_addr = self.get_client_ip_address(request)

        return ClientApiRequest(
            client_id=ip_addr
            method=ApiMethod.GET
            api_name=''
        )
    def __call__(self, request):
        RateLimitingService.verify_api_limit(request)
        return response