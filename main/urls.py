from django.urls import path
from . import views
urlpatterns = [
    path("<int:id>", views.frontpage, name='frontpage'),
    path("", views.home, name = "home")
]