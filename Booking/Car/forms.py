from django import forms
from .models import *

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = "__all__"


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = ProductAdd
        # fields = ['car_name', 'car_color', 'amt_per_km', 'discount_per', 'image1', 'image2', 'image3', 'image4', 'image5']
        # fields = "__all__"
        exclude = ["dealer_id"]
