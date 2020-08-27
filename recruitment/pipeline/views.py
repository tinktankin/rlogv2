from django.shortcuts import render
from .models import Pipeline_class
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from django.template import RequestContext

# Create your views here.

def pipeline(request):
    #return render(request, "excel_pipeline.html", {'result': df})
    return render(request, 'pipeline/pipeline_html.html');
    excel_import(request)


def excel_import(request):
    if request.method == "Post":
        uploaded_file = request.FILES['document']
        val1 = str(request.GET['num1'])
        val2 = str(request.GET['num2'])
        val3 = str(request.GET['num3'])
        val4 = str(request.GET['num4'])
        val5 = str(request.GET['num5'])
        val6 = str(request.GET['num6'])
        val7 = str(request.GET['num7'])
        val8 = str(request.GET['num8'])
        val9 = str(request.GET['num9'])
        val10 = str(request.GET['num10'])
        val11 = str(request.GET['num11'])
        val12 = str(request.GET['num12'])
        val13 = str(request.GET['num13'])
        val14 = str(request.GET['num14'])
        val15 = str(request.GET['num15'])
        val16 = str(request.GET['num16'])
        val17 = str(request.GET['num17'])
        val18 = str(request.GET['num18'])
        val19 = str(request.GET['num19'])
        val20 = str(request.GET['num20'])
        val21 = str(request.GET['num21'])
        val22 = str(request.GET['num22'])
        val23 = str(request.GET['num23'])
        val24 = str(request.GET['num24'])
        val25 = str(request.GET['num25'])
        val26 = str(request.GET['num26'])
        val27 = str(request.GET['num27'])
        val28 = str(request.GET['num28'])
        val29 = str(request.GET['num29'])
        val30 = str(request.GET['num30'])
        val31 = str(request.GET['num31'])
        val32 = str(request.GET['num32'])
        val33 = str(request.GET['num33'])
        cols = [val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,val21,val22,val23,val24,val25,val26,val27,val28,val29,val30,val31,val32,val33]
        df = pd.read_excel(request.files.get('document'), usecols=cols)
        #fd = pd.head(n=1)
        #print(fd)
        t = df.isnull()
        if t is "True":
            t = df.isnumeric()
            if t is "True":
                df = df.fillna(0)
            else:
                df = df.fillna("NA")
        df = df.fillna("NA")
        engine = create_engine('postgresql://postgres:rasika@localhost:5432/Pipeline')

        df.to_sql(name='pipeline_pipeline_class', con=engine, if_exists='replace', index=False)
    return render(request, "pipeline/excel_pipeline.html", {'result':'Done'})

def mapping(request):
    Pipeline_class.Recruiter == str(request.GET['num1'])
    Pipeline_class.Client == str(request.GET['num2'])
    Pipeline_class.Position == str(request.GET['num3'])
    Pipeline_class.Recruiter_date == str(request.GET['num4'])
    Pipeline_class.CV_sub_date == str(request.GET['num5'])
    Pipeline_class.Candidate_name == str(request.GET['num6'])
    Pipeline_class.Current_status_no == str(request.GET['num7'])
    Pipeline_class.Current_status_descr == str(request.GET['num8'])
    Pipeline_class.Interview_date == str(request.GET['num9'])
    Pipeline_class.Remarks == str(request.GET['num10'])
    Pipeline_class.Profile_skills == str(request.GET['num11'])
    Pipeline_class.Current_org == str(request.GET['num12'])
    Pipeline_class.Qualification == str(request.GET['num13'])
    Pipeline_class.Experience == str(request.GET['num14'])
    Pipeline_class.Current_Loc == str(request.GET['num15'])
    Pipeline_class.Contact_no == str(request.GET['num16'])
    Pipeline_class.Alternate_contact_no == str(request.GET['num17'])
    Pipeline_class.Email_id == str(request.GET['num18'])
    Pipeline_class.Current_salary == str(request.GET['num19'])
    Pipeline_class.Expected_salary == str(request.GET['num20'])
    Pipeline_class.Notice_period == str(request.GET['num21'])
    Pipeline_class.Offer_date == str(request.GET['num22'])
    Pipeline_class.Offer_amount == str(request.GET['num23'])
    Pipeline_class.Joining_date == str(request.GET['num24'])
    Pipeline_class.Vacancy_code == str(request.GET['num25'])
    Pipeline_class.Applicant_code == str(request.GET['num26'])
    Pipeline_class.Birth_date == str(request.GET['num27'])
    Pipeline_class.Birth_month == str(request.GET['num28'])
    Pipeline_class.Birth_year == str(request.GET['num29'])
    Pipeline_class.Preferred_company == str(request.GET['num30'])
    Pipeline_class.Preferred_Loc == str(request.GET['num31'])
    Pipeline_class.Week_no == str(request.GET['num32'])
    Pipeline_class.Year == str(request.GET['num33'])


def equ(request):
    val1 = str(request.GET['num1'])
    val2 = str(request.GET['num2'])
    val3 = str(request.GET['num3'])
    val4 = str(request.GET['num4'])
    val5 = str(request.GET['num5'])
    val6 = str(request.GET['num6'])
    val7 = str(request.GET['num7'])
    val8 = str(request.GET['num8'])
    val9 = str(request.GET['num9'])
    val10 = str(request.GET['num10'])
    val11 = str(request.GET['num11'])
    val12 = str(request.GET['num12'])
    val13 = str(request.GET['num13'])
    val14 = str(request.GET['num14'])
    val15 = str(request.GET['num15'])
    val16 = str(request.GET['num16'])
    val17 = str(request.GET['num17'])
    val18 = str(request.GET['num18'])
    val19 = str(request.GET['num19'])
    val20 = str(request.GET['num20'])
    val21 = str(request.GET['num21'])
    val22 = str(request.GET['num22'])
    val23 = str(request.GET['num23'])
    val24 = str(request.GET['num24'])
    val25 = str(request.GET['num25'])
    val26 = str(request.GET['num26'])
    val27 = str(request.GET['num27'])
    val28 = str(request.GET['num28'])
    val29 = str(request.GET['num29'])
    val30 = str(request.GET['num30'])
    val31 = str(request.GET['num31'])
    val32 = str(request.GET['num32'])
    val33 = str(request.GET['num33'])
    mapping(request)







