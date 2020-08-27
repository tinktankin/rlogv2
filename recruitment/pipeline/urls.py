from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.pipeline, name='pipeline'),
    path('excel_import/',views.excel_import, name='excel_import')

]