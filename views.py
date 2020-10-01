from django.shortcuts import render, redirect
from .models import Mandate
from .resources import JobResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse, JsonResponse
from .forms import MandateForm
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json
import os
import datetime
from pprint import pprint
#  from django.contrib.staticfiles.templatetags.staticfiles import static # no such file
from django.forms.models import model_to_dict
# from django.contrib.auth.views import login,logout # cannot import name 'login' from 'django.contrib.auth.views'

# Create your views here.
CSV_STORAGE = os.path.join(os.getcwd(), 'database', 'static', 'csv')


@csrf_exempt
def import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students) #make sure that there' no header
        path_name = os.path.join('database', 'static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/fieldmatching?df='+ path_name)
    else:
        return render(request, 'import_data.html')


def fieldmatching(request):   
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Mandate._meta.get_fields()]
        if request.POST.get('checkBox') == None:   
        #  To keep the same columns in case of matching 'fields' and ###'names', add a checkbox on the html page
            matched = { key:request.POST.get(key, False) for key in fields }
            new_dict = dict([(value, key) for key, value in matched.items()])
            df.rename(columns = new_dict, inplace = True)
        #  df.drop('id', axis=1, inplace=True) # Drop Remove rows or columns by specifying label names and corresponding axis, or by specifying directly index or column names. When using a multi-index, labels on different levels can be removed by specifying the level.
        #  Set the DataFrame index (row labels) using one or more existing columns or arrays (of the correct length). The index can replace the existing index or expand on it.
        #  "None of ['apple', 'ball', 'cat', 'dog', 'eagle', 'fox', 'gorrila', 'hen', 'int', 'jet', 'kite', 'lamba', 'mamba', 'next', 'o', 'p'] are in the columns"
        #  Convert the DataFrame to a dictionary. orientation 
        #  df.to_dict('index') return this > {'row1': {'col1': 1, 'col2': 0.5}, 'row2': {'col1': 2, 'col2': 0.75}} 
    
        df.set_index('id', drop=True, inplace=True)
        dictionary = df.to_dict(orient="index")
        print(dictionary)
    
        for index, object in dictionary.items():
            # model = MODEL_NAME()
            model = Mandate()
            for key,value in object.items():
                setattr(model, key, value)
            setattr(model, 'id', index)
            model.save()
        return render(request, 'import_data.html')
# i m getting an error when in use return redirect('import_data')
    else:
        path_name = request.GET.get('df')
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Mandate._meta.get_fields()]
        return render(request, 'fieldmatching.html', {'fields' : names, 'path_name': path_name, 'names' : fields})
    
    
    
    
    
        

        
         
         
        
        
        
        
        
        
         
       
