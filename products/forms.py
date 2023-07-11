from django import forms

class ProductForm(forms.Form):
    p_name = forms.CharField(label='Name of your product', max_length=100)
    p_price = forms.IntegerField(label="Price of your product")
    p_desc = forms.CharField(label="Items description", max_length=255)
    p_owner = forms.CharField(label="Owner of item", max_length=100)
    p_stock = forms.IntegerField(label="Number of available copies of said item")
    p_category = forms.CharField(label="Category of the item", max_length=120)