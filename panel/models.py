from django.db import models


class Company(models.Model):
    name     =  models.CharField(max_length=60, verbose_name="Company Name * ",                                    blank=False)
    email    =  models.EmailField(max_length=60)
    logo     =  models.FileField(upload_to='uploads/', blank=True)
    website  =  models.URLField(max_length=100)
    class Meta:
        # ordering = ["name"]
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name  = models.CharField(max_length=60, verbose_name="First Name * ",                                      blank=False)
    last_name   = models.CharField(max_length=60, verbose_name="Last Name * ",                                       blank=False)
    company     = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True,                                  blank=True, related_name='companies')
    email       = models.EmailField(max_length=60) 
    phone       = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name
