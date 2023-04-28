from django.shortcuts import render
from django.views.generic import TemplateView
from .functions import multiplicate_by_5
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ProductForm
from .models import Product



# Create your views here.
@login_required
def home_page(request):
    return render(request, 'main/home_page.html')

# @login_required
# def user_history(request):


#     context = {
#         "product_database" : Product.objects.filter(user_id=request.user),
#     }


#     return render(request, 'main/user_history.html', context=context)

class User_History_page(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {
            "product_database" : Product.objects.filter(user_id=request.user),
        }
        # print(list(request.GET.keys())[0])
        print('get method')
        print(request.POST)
        # if request.GET.keys() == 
        return render(request, 'main/user_history.html', context=context)
    
    def post(self, request, *args, **kwargs):

        # Delete function
        print('Delete function')
        # print(product_id)

        context = {
            "product_database" : Product.objects.filter(user_id=request.user),
        }
        # print(request.POST)
        return render(request, 'main/user_history.html', context=context)

    # def delete(self, request, *args, **kwargs):
    #     context = {
    #         "product_database" : Product.objects.filter(user_id=request.user),
    #     }
    #     print('delete method')
    #     return render(request, 'main/user_history.html', context=context)

# @login_required
# def predict_page(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form = ProductForm()
#     return render(request, 'main/prediction.html', {'form': form})
class Predict_page(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/prediction.html')

    def post(self, request, *args, **kwargs):
        user = request.user
        print(user)
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = user
            product.save()
            # form.user = get_user_model()
            # form.save(user=get_user_model())
        else:
            print('form is not correct')
            print(form.errors)
            form = ProductForm()
        return render(request, 'main/prediction.html', {'form': form})

@login_required
def admin_user_database_page(request):
    user_database = get_user_model()
    context = {
        "user_database" : user_database.objects.all(),
    }
    
    return render(request, 'main/user_database.html', context=context)

@login_required
def testing_page(request, product_id):
    print(product_id)
    # Delete this product_id
    Product.objects.filter(id=product_id).delete()

    context = {
            "product_database" : Product.objects.filter(user_id=request.user),
        }
        # print(request.POST)
    return render(request, 'main/user_history.html', context=context)

    # return render(request, 'main/user_database.html', context=context, id=id)

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