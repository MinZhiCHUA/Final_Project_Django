from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    # path('multi', views.multi_func, name="multi"),
    # path('product', views.tmp_product, name="product"),
    path('user_history', login_required(views.User_History_page.as_view()), name="user_history"),
    # MZ removing the old prediction page
    path('prediction', login_required(views.Predict_page_bento_api.as_view()), name="predict_page"),
    path('user_prediction_management', login_required(views.user_prediction_management_page), name="user_prediction_management"),
    path('user_database', views.admin_user_database_page, name="user_database"),
    path('delete_user/<int:user_id>', views.delete_user_page, name="delete_user"),
    path('delete_prediction/<int:product_id>', views.delete_prediction_page, name="delete_prediction"),
    path('signup/', views.signup, name='signup'),
    path('admin_user_predict_history/<int:user_id>', views.admin_user_predict_history, name="admin_user_predict_history"),

    
    
]