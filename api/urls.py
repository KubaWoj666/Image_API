from django.urls import path
from . import views

urlpatterns = [
    path("", views.ImageListCreateAPIView.as_view(), name="list-view"),
    path("<int:pk>", views.ImageDetailAPIView.as_view(), name="detail-view")
    
]