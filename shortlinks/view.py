from django.shortcuts import redirect, get_object_or_404

from shortlinks.models import Links
from shortlinks.tasks import update_request_count_task


def link(request, id):
    db_id = Links.decode(id)
    link_db = get_object_or_404(Links, id=db_id, active=True, status=True)
    update_request_count_task.apply_async((db_id,))
    return redirect(link_db.link)
