import shortuuid

from shortner.models import URL


def create_tiny_url(url):
    short_url, created = URL.objects.get_or_create(source_url=url)
    if created:
        short_url.tiny_url = shortuuid.uuid()
        short_url.save(update_fields=['tiny_url'])
    return short_url.get_url_data()
