
from django.http import JsonResponse
from django.views import View
from django.shortcuts import redirect
from .models import URL
from .services import create_tiny_url


class CreateLink(View):
    """
    This is creating tiny url from original url
    """
    def post(self, request, *args, **kwargs):
        data = request.POST
        if not data.get('url'):
            return JsonResponse({'error': 'Pass original url in url parameter'}, status=400)
        tiny_url_data = create_tiny_url(data.get('url'))
        return JsonResponse({'tiny_url': tiny_url_data.as_dict()})


class RedirectLink(View):
    """
    This View Convert tiny url to original url
    Redirect to the Original url
    """
    def get(self, request, url):
        try:
            url_obj = URL.objects.get(tiny_url=url)
        except URL.DoesNotExist:
            return JsonResponse({'error': 'Tiny URL does not exist'}, status=404)
        return redirect(url_obj.source_url)
