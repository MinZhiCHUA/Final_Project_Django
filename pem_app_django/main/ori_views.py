from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .functions import multiplicate_by_5
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ProductForm, SignUpForm
from .models import Product

from django.urls import reverse_lazy
# from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User

from django.conf import settings



from requests import Request, Session
import json



# Create your views here.
@login_required
def home_page(request):
    return render(request, 'main/home_page.html')

class User_History_page(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {
            "product_database" : Product.objects.filter(user_id=request.user),
        }

        return render(request, 'main/user_history.html', context=context)
    
    def post(self, request, *args, **kwargs):

        product_full=Product.objects.filter(user_id=request.user)
        

        context = {
            "product_database" : Product.objects.filter(user_id=request.user),
        }

        return render(request, 'main/user_history.html', context=context)


class Predict_page(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/prediction.html')

    def post(self, request, *args, **kwargs):
        # TODO: set up the url for api
        url = "http://127.0.0.1:8000/"
        # url = "http://127.0.0.1:3000/"

        session = Session()

        user = request.user
        # print(user)
        form = ProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            # request a respose from api
            response = session.post(url, json=form.cleaned_data)

            info = response.text
            info = json.loads(info)

            print(info['predictions'])

            product = form.save(commit=False)
            product.user = user

            product.pred_label_text = info['predictions']
            
            product.save()

        return render(request, 'main/prediction.html')
    
class Predict_page_bento_api(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/prediction.html')

    def post(self, request, *args, **kwargs):
        # TODO: set up the url for api
        url = "http://127.0.0.1:8000/"
        # url = "http://127.0.0.1:3000/"

        session = Session()

        user = request.user
        # print(user)
        form = ProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            # request a respose from api
            response = session.post(url, json=form.cleaned_data)

            info = response.text
            info = json.loads(info)

            print(info['context'])

            product = form.save(commit=False)
            product.user = user
            product.pred_label_text = info['predictions']
            product.save()

        return render(request, 'main/prediction_api.html')

@login_required
def admin_user_database_page(request):
    user_database = get_user_model()
    context = {
        "user_database" : user_database.objects.all(),
    }
    
    return render(request, 'main/user_database.html', context=context)

@login_required
def delete_user_page(request, user_id):

    print("Delete User Page")
    User.objects.filter(id=user_id).delete()

    user_database = get_user_model()
    context = {
        "user_database" : user_database.objects.all(),
    }
    return render(request, 'main/user_database.html', context=context)

@login_required
def delete_prediction_page(request, product_id):

    Product.objects.filter(id=product_id).delete()
    context = {
            "product_database" : Product.objects.filter(user_id=request.user),
        }

    return render(request, 'main/user_history.html', context=context)


def multi_func(request):
    weekdays = [
        'lundi',
        'mardi',
        'mercredi',
        'jeudi',
        'vendredi',
        'samedi',
        'dimanche',
    ]

    context = {
        "test" : multiplicate_by_5(5),
        "weekdays":weekdays
    }
    
    return render(request, 'temp/multi_func.html', context = context)

def tmp_product(request):
    return render(request, 'temp/product.html')

def signup(request):
   
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print(form)
        if form.is_valid():
            print("FORM IS VALID")
            print(form.cleaned_data.get('username'))
            user = User.objects.create_user(form.cleaned_data.get('username'), form.cleaned_data.get('password1'))

            user_database = get_user_model()
            context = {
                "user_database" : user_database.objects.all(),
            }

            return render(request, 'main/user_database.html', context=context)
    else: 
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
