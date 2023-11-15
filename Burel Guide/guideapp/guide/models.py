from django.db import models


class guide(models.Model):
     company_name=models.CharField(max_length=200)     
     company_gsm=models.CharField(max_length=12) 
     
     
     
