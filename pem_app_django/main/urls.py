from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('multi', views.multi_func, name="multi"),
    path('product', views.tmp_product, name="product"),
    # path('user_history', views.user_history, name="user_history"),
    path('user_history', login_required(views.User_History_page.as_view()), name="user_history"),
    path('prediction', login_required(views.Predict_page.as_view()), name="predict_page"),
    path('prediction_api', login_required(views.Predict_page_bento_api.as_view()), name="predict_page_api"),
    path('user_database', views.admin_user_database_page, name="user_database"),
    path('delete_user/<int:user_id>', views.delete_user_page, name="delete_user"),
    path('delete_prediction/<int:product_id>', views.delete_prediction_page, name="delete_prediction"),
    path('signup/', views.signup, name='signup'),
    # login_required(views.UserProfileDetailView.as_view()), name='test')
    # path('stores/<int:store_id>/',...)
    
]