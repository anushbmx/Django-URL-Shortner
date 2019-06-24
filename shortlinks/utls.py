from shortlinks.models import Links
from django.db.models import F


def update_request_count(link_id):
    Links.objects.filter(id=link_id).update(hits=F('hits') + 1)
