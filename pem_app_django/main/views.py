from django.shortcuts import render
from .functions import multiplicate_by_5
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home_page(request):
    return render(request, 'main/home_page.html')

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