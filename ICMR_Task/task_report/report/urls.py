
from django.urls import path
from . import views
from .views import download_csv


urlpatterns = [
    path('', views.report_list, name='report_list'),
    
    path('create/', views.report_create, 
            name='report_create'),
    path('<int:report_id>/edit/', views.report_edit, 
        name='report_edit'),
    path('<int:report_id>/delete/', views.report_delete, 
        name='report_delete'),
    path('register/', views.register, 
        name='register'),

    # path('login/', views.login, 
    #     name='login'),

    path('download/', download_csv, name='download_csv'),

    

    
]
