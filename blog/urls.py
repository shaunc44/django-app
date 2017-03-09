from django.conf.urls import url
from . import views

# ^$ will match an empty string
urlpatterns = [
	url(r'^$', views.post_list, name = 'post_list'),
]