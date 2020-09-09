from django.shortcuts import render, redirect
from .forms import Pipeline_class_form
from .models import Pipeline_class
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json
import datetime
from pprint import pprint
from django.forms.models import model_to_dict

# Create your views here.
CSV_STORAGE = os.path.join(os.getcwd(), 'pipeline', 'static', 'csv')


@csrf_exempt
def import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('pipeline', 'static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/fieldmatching?df=' + path_name)
    else:
        return render(request, 'import_data.html')


# def pipeline(request):
# return render(request, 'pipeline/pipeline_html.html');
# excel_import(request)


# def excel_import(request):
# if request.method == "Post":
# uploaded_file = request.FILES['document']
# df = pd.read_excel(uploaded_file)
# path_name = uploaded_file.name
# val34 = str(request.GET['num34'])
# val1 = str(request.GET['num1'])
# val2 = str(request.GET['num2'])
# val3 = str(request.GET['num3'])
# val4 = str(request.GET['num4'])
# val5 = str(request.GET['num5'])
# val6 = str(request.GET['num6'])
# val7 = str(request.GET['num7'])
# val8 = str(request.GET['num8'])
# val9 = str(request.GET['num9'])
# val10 = str(request.GET['num10'])
# val11 = str(request.GET['num11'])
# val12 = str(request.GET['num12'])
# val13 = str(request.GET['num13'])
# val14 = str(request.GET['num14'])
# val15 = str(request.GET['num15'])
# val16 = str(request.GET['num16'])
# val17 = str(request.GET['num17'])
# val18 = str(request.GET['num18'])
# val19 = str(request.GET['num19'])
# val20 = str(request.GET['num20'])
# val21 = str(request.GET['num21'])
# val22 = str(request.GET['num22'])
# val23 = str(request.GET['num23'])
# val24 = str(request.GET['num24'])
# val25 = str(request.GET['num25'])
# val26 = str(request.GET['num26'])
# val27 = str(request.GET['num27'])
# val28 = str(request.GET['num28'])
# val29 = str(request.GET['num29'])
# val30 = str(request.GET['num30'])
# val31 = str(request.GET['num31'])
# val32 = str(request.GET['num32'])
# val33 = str(request.GET['num33'])
# cols = [val34, val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15, val16,
# val17, val18, val19, val20, val21, val22, val23, val24, val25, val26, val27, val28, val29, val30, val31,
# val32, val33
# ]
# df = pd.read_excel(uploaded_file)
# df.rename(columns={Pipeline_class.Recruiter: val1, Pipeline_class.Client: val2, Pipeline_class.Position: val3,
# Pipeline_class.Recruiter_date: val4, Pipeline_class.CV_sub_date: val5,
# Pipeline_class.Candidate_name: val6, Pipeline_class.Current_status_no: val7,
# Pipeline_class.Current_status_descr: val8, Pipeline_class.Interview_date: val9,
# Pipeline_class.Remarks: val10, Pipeline_class.Profile_skills: val11,
# Pipeline_class.Current_org: val12, Pipeline_class.Qualification: val13,
# Pipeline_class.Experience: val14, Pipeline_class.Current_Loc: val15,
# Pipeline_class.Contact_no: val16, Pipeline_class.Alternate_contact_no: val17,
# Pipeline_class.Email_id: val18, Pipeline_class.Current_salary: val19,
# Pipeline_class.Expected_salary: val20, Pipeline_class.Notice_period: val21,
# Pipeline_class.Offer_date: val22, Pipeline_class.Offer_amount: val23,
# Pipeline_class.Joining_date: val24, Pipeline_class.Vacancy_code: val25,
# Pipeline_class.Applicant_code: val26, Pipeline_class.Birth_date: val27,
# Pipeline_class.Birth_month: val28, Pipeline_class.Birth_year: val29,
# Pipeline_class.Preferred_company: val30, Pipeline_class.Preferred_Location: val31,
# Pipeline_class.Week_no: val32, Pipeline_class.Year: val33,
# Pipeline_class.Id: val34,})

# df.to_excel(path_name, index=False)
# fieldmatching(request)

# engine = create_engine('postgresql://postgres:rasika@localhost:5432/pipe')
# df.to_sql(name='pipeline_pipeline_data', con=engine, if_exists='replace', index=True)
# return render(request, "pipeline/excel_pipeline.html", {'result': 'Done'})


def fieldmatching(request):
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        names = list(df.columns)
        if request.POST.get('checkBox') == None:
            matched = {key: request.POST.get(key, False) for key in names}
            df.rename(columns=matched, inplace=True)
        #df.drop('id', axis=1, inplace=True)
        df.set_index("id", drop=True, inplace=True)

        dictionary = df.to_dict(orient="index")
        for index, object in dictionary.items():
            m = Pipeline_class()
            for k, v in object.items():
                setattr(m, k, v)
            setattr(m, 'id', index)
            m.save()
        return render(request, 'pipeline/import_data.html')
    else:
        path_name = request.GET.get('df')
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Pipeline_class._meta.get_fields()]
        return render(request, 'fieldmatching.html',
                      {'fields': fields, 'path_name': path_name, 'names': names})
