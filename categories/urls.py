from django.urls import path
from categories.views import CategoryListView, SubCategoryListView


urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('<int:category_id>/sub_categories/', SubCategoryListView.as_view(), name='sub_categories_list')
]
