from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("qrcode.html/",qrcode),
    path("random.html/",passgen),
    path("qrcode.html/home.html",home),
]