import re

from django.conf import settings
from django.contrib.auth.decorators import login_required


class RequireLoginMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.required = [
            re.compile(url) for url in settings.LOGIN_REQUIRED_URLS
        ]
        self.exceptions = [
            re.compile(url) for url in settings.LOGIN_REQUIRED_URLS_EXCEPTIONS
        ]

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_active:
            return None

        for url in self.exceptions:
            if url.match(request.path):
                return None

        for url in self.required:
            if url.match(request.path):
                return login_required(view_func)(
                    request,
                    *view_args,
                    **view_kwargs
                )

        return None
