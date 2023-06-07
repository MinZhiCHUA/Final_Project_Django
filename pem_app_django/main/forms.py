from django import forms
# from .models import ApiModel
from .models import Product, Feedback, User
# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# User = get_user_model()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description']
        labels = {'fullname': "Title", "description": "Description"}

        # def form_valid(self, form):
        #     form.instance.created_by = self.request.user
#         #     return super().form_valid(form)

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta) :
        model = User
        fields = ['username', 'password1', 'password2']

# class UserCreationFromCustom(UserCreationForm):
#     class Meta(UserCreationForm.Meta) :
#         fields = ['username', 'password1', 'password2', 'email']


# class ApiForm(forms.ModelForm):
#     class Meta :
#         model = ApiModel
#         fields = '__all__'
#         labels = {
#             'title' : "Entrez votre crypto ici",
#             'description': "Entrez votre devise ici"
#                   }