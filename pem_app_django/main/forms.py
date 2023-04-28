from django import forms
from .models import Product, Feedback

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description']
        labels = {'fullname': "Title", "description": "Description"}

        # def form_valid(self, form):
        #     form.instance.created_by = self.request.user
        #     return super().form_valid(form)