from dal import autocomplete

from django import forms

from .models import FcUser, Product


class UsageStatsForm(forms.Form):
    is_known_product = forms.BooleanField(required=False, initial=True)
    is_known_article = forms.BooleanField(required=False, initial=True)
    user = forms.ModelChoiceField(
        queryset=FcUser.objects.all().order_by('username'),
        widget=autocomplete.ModelSelect2(),
        required=False,
    )
    product = forms.ModelChoiceField(
        label='product',
        required=False,
        queryset=Product.objects.filter(is_real=True).order_by('product_key'),
        widget=autocomplete.ModelSelect2()
    )
    from_date = forms.DateField(
        label='From Date',
        required=False,
        widget=forms.TextInput(attrs={'class': 'datepicker'})
    )
    to_date = forms.DateField(
        label='To Date',
        required=False,
        widget=forms.TextInput(attrs={'class': 'datepicker'})
    )
