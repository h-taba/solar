from django.db import models

class Employees(models.Model):
    """"
    First_Name Last_Name Job_Title E_mail
    Business_Phone Home_Phone Mobile_Phone Fax_Number Address 
    City Company State_Province ZIP_PostalCode Country_Region Notes
    
    """

    First_Name = models.CharField(max_length=50)
    Last_Name= models.CharField(max_length=50)
    Job_Title= models.CharField(max_length=50)
    E_mail= models.CharField(max_length=50)
    Business_Phone= models.CharField(max_length=25)
    Home_Phone= models.CharField(max_length=25)
    Mobile_Phone= models.CharField(max_length=25)
    Fax_Number=models.CharField(max_length=25)
    Address=models.CharField(max_length=25)
    City=models.CharField(max_length=50)
    Company= models.CharField(max_length=50)
    State_Province= models.CharField(max_length=50)
    ZIP_PostalCode= models.CharField(max_length=50)
    Country_Region= models.CharField(max_length=50)
    Notes= models.CharField(max_length=250)
    