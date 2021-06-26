from django.urls import path
from . import views

app_name = "imageprocessor"


urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.create, name="create"),
    path("update/<int:image_id>/", views.update, name="update"),
    path("successful/", views.success, name="success"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
