from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("saveq/", views.add_question, name="save"),
    path("articles/<int:year>/<int:month>/", views.month_archive),
]