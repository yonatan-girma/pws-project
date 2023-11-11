from django import forms
from assets.models import Asset
from categories.models import Category, SubCategory


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Asset Name'
        self.fields['category'].empty_label = 'Select Category'
        self.fields['sub_category'].empty_label = 'Select Sub-Category'
