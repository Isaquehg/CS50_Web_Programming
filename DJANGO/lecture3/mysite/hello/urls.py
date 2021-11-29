from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("isaque", views.isaque, name="isaque"),
    path("bruna", views.bruna, name="bruna")
]