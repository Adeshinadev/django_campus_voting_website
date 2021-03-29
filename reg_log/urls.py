from django.urls import path
from reg_log import views
urlpatterns=[
    path('register',views.register,name='register'),
    path('check_result',views.check_result,name='check_result'),
    path('final_reg',views.final_reg,name='final_reg'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard')
]