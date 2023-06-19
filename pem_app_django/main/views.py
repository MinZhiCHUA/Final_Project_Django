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


# To access deployed endpoint
from typing import Dict, List, Union
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value



# Create your views here.
@login_required
def home_page(request):
    print ("something something")
    return render(request, 'main/home_page.html')

class User_History_page(TemplateView):
    def get(self, request, *args, **kwargs):

        product_full_list = Product.objects.filter(user_id=request.user)
        # print("I want to print something here")

        # print(product_full_list[0].pred_label_text)

        # pred_json = dict()
        
        # for idx, product_single in enumerate(product_full_list):
        #     print(idx)
        #     pred_single = json.loads(product_single.pred_label_text) 
        #     pred_json[idx] = pred_single

        # # print (pred_json)

        # print(product_full_list[0].pred_label_json[0]["attribute_code"])


        # for id_single_product, single_prorduct in enumerate(product_full_list):
        #     for id_single_pred, single_pred in single_prorduct.pred_label_json:
        #         print(single_pred)
        #         print (idx)

        
        
        context = {
            "product_database" : product_full_list,
        }

        return render(request, 'main/user_history.html', context=context)
    
    def post(self, request, *args, **kwargs):
        product_full_list = Product.objects.filter(user_id=request.user)
        print("I want to print something here")

        print(product_full_list[0])

        
        # for single_product in product_full_list:
    

        context = {
            "product_database" : product_full_list,
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
        return render(request, 'main/prediction_api.html')

    def post(self, request, *args, **kwargs):
        session = Session()

        user = request.user

        form = ProductForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)

            input_file = form.cleaned_data
            input_file["attribute_code"]="00000"

            # print(input_file)

            # request a respose from api
            predictions = predict_custom_trained_model_sample(
                project="artefact-taxonomy",
                endpoint_id="2845017123195977728",
                location="europe-west1",
                # instances={
                #     "title": "CORNIERE ALU BLANC 2.35X4.35X0.15CM 2.5M",
                #     "description": "",
                #     "attribute_code": "10837" # TODO: why must I provide this??
                # }
                instances=input_file
            ) 

            # for prediction in predictions:
            #     print(" prediction:", dict(prediction))

            # Opening JSON file
            f = open('static/lov_code_map_FR.json')
            g = open('static/step_model_label.json')
            
            # returns JSON object as 
            # a dictionary
            lov_code_label = json.load(f)
            step_model_label = json.load(g)

            list_prediction = []
            for prediction in predictions:
                pred_1 = dict(prediction)
                if pred_1['attribute_code'] != 'Product Class':
                    pred_1['label'] = lov_code_label[pred_1['label']]
                else:
                    pred_1['label'] = step_model_label[pred_1['label']]
                    # print(type(pred_1['label']))
                list_prediction.append(pred_1)

            # print(list_prediction)


            product = form.save(commit=False)
            product.user = user
            product.pred_label_text = json.dumps(list_prediction)
            product.pred_label_json = list_prediction
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


def predict_custom_trained_model_sample(
    project: str,
    endpoint_id: str,
    instances: Union[Dict, List[Dict]],
    location: str = "us-central1",
    api_endpoint: str = "europe-west1-aiplatform.googleapis.com",
):
    """
    `instances` can be either single instance of type dict or a list
    of instances.
    """
    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    # The format of each instance should conform to the deployed model's prediction input schema.
    instances = instances if type(instances) == list else [instances]
    instances = [
        json_format.ParseDict(instance_dict, Value()) for instance_dict in instances
    ]
    parameters_dict = {}
    parameters = json_format.ParseDict(parameters_dict, Value())
    endpoint = client.endpoint_path(
        project=project, location=location, endpoint=endpoint_id
    )
    response = client.predict(
        endpoint=endpoint, instances=instances, parameters=parameters
    )
    print("response")
    print(" deployed_model_id:", response.deployed_model_id)
    # The predictions are a google.protobuf.Value representation of the model's predictions.
    predictions = response.predictions
    # for prediction in predictions:
    #     print(" prediction:", dict(prediction))

    return predictions