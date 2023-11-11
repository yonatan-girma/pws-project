from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from assets.forms import AssetForm
from assets.models import Asset
from categories.models import SubCategory


class AssetListView(LoginRequiredMixin, ListView):
    model = Asset

    def get_queryset(self):
        return Asset.objects.filter(sub_category_id=self.kwargs['sub_category_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'sub_category': SubCategory.objects.get(id=self.kwargs['sub_category_id']), 'title': 'Assets'})
        return context


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Asset'
        return context

    def get_success_url(self):
        return reverse('assets:list', kwargs={'sub_category_id': self.object.sub_category.id})


class AssetDetailView(LoginRequiredMixin, DetailView):
    model = Asset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Asset'
        return context


class AssetUpdateView(LoginRequiredMixin, UpdateView):
    model = Asset
    form_class = AssetForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Asset'
        return context

    def get_success_url(self):
        return reverse('assets:detail', kwargs={'sub_category_id': self.object.sub_category.id, 'pk': self.object.id})


class AssetDeleteView(LoginRequiredMixin, DeleteView):
    http_method_names = ['post']
    model = Asset

    def get_success_url(self):
        return reverse('assets:list', kwargs={'sub_category_id': self.object.sub_category.id})
