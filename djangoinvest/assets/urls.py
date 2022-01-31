from django.urls import path

from . import views

app_name = "assets"

urlpatterns = [
    path('', views.AssetListView.as_view(), name='list'),
    path('<int:pk>/', views.AssetDetailView.as_view(), name='detail'),
]
