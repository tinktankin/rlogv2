from django.db import models

# Create your models here.
class Mandate_class(models.Model):
    Job_id = models.IntegerField(null=True)
    Company_name = models.CharField(max_length=150)
    Manager_name = models.CharField(max_length=50)
    Category_job = models.CharField(max_length=30)
    No_of_openings = models.IntegerField(null=True)
    Experience = models.IntegerField(null=True)
    Designation = models.CharField(max_length=30)
    Eligibility = models.TextField()
    Salary = models.IntegerField(null=True)
    Application_start_date = models.DateField(null=True)
    Application_end_date = models.DateField(null=True)
    Required_skills = models.TextField()
    Roles_Responsibility = models.TextField()


