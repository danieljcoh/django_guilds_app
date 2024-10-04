from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="guild_posts_app_home"),
    path("<int:post_id>", views.post_details, name="post_details")
]