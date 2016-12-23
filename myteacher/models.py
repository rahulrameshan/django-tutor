from django.db import models
class Quotes(models.Model):
    quote_heading=models.CharField(max_length=100,null=True)
    quote_contents=models.CharField(max_length=200,null=True)

# Create your models here.
