from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from categories.models import Category, SubCategory


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categories'
        return context


class SubCategoryListView(LoginRequiredMixin, ListView):
    model = SubCategory

    def get_queryset(self):
        return SubCategory.objects.filter(category_id=self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sub-Categories'
        return context

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return JsonResponse(
                {'sub_categories': list(SubCategory.objects.filter(category_id=kwargs['category_id']).values('id', 'title'))})
        return super().get(request, *args, **kwargs)
