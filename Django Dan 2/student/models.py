from django.db import models

class StudentOrganization(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    organization = models.ForeignKey(StudentOrganization, on_delete=models.DO_NOTHING)
    index = models.CharField(max_length=50, db_index=True)
   

    


