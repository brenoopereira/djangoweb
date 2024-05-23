from django.urls import path
from . import views

urlpatterns = [
    path("gatherings/", views.GatheringListCreate.as_view(), name="gathering-list"),
    path("gatherings/delete/<int:pk>/", views.GatheringDelete.as_view(), name="delete-gathering"),
]