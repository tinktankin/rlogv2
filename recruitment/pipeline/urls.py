from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    #path('',views.pipeline, name='pipeline'),
    #path('excel_import',views.excel_import, name='excel_import'),
    #path('fieldmatching',views.fieldmatching, name='fieldmatching'),
    path('import', views.import_data),
    path('fieldmatching', views.fieldmatching)
]
