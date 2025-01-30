from django.db import models

# Create your models here.

class tbl_category(models.Model):
    category_name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)