from django.conf.urls import url

from ..views.admin import ImageAdminAPI

urlpatterns = [
    url(r"^image/?$", ImageAdminAPI.as_view(), name="image_admin_api"),
]