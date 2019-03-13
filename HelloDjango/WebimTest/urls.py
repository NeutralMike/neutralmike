from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'vk-auth', views.vk_auth),
    url(r'', views.test)
]
