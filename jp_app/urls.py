from django.urls import path
from jp_app import views

urlpatterns=[
    path('signup',views.SignUpView.as_view(),name='signup'),
    path('login',views.SigninView.as_view(),name='login'),

]