
from .models import URL
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View


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
