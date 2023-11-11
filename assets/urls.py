from django.urls import path
from assets.views import AssetListView, AssetCreateView, AssetDetailView, AssetUpdateView, AssetDeleteView


urlpatterns = [
    path('sub_categories/<int:sub_category_id>/assets/', AssetListView.as_view(), name='list'),
    path('sub_categories/<int:sub_category_id>/assets/<int:pk>/', AssetDetailView.as_view(), name='detail'),
    path('sub_categories/<int:sub_category_id>/assets/<int:pk>/edit/', AssetUpdateView.as_view(), name='update'),
    path('sub_categories/<int:sub_category_id>/assets/<int:pk>/delete/', AssetDeleteView.as_view(), name='delete'),
    path('assets/new/', AssetCreateView.as_view(), name='create'),
]
