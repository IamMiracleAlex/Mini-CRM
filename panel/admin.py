from django.contrib import admin

from . models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        
        ('Company information', {'fields': ['name','email','logo','website']})
    ]

    list_display = ('name', 'email', 'logo', 'website')
    list_filter = ['name']

    search_fields = ['name']
    list_per_page = 10

   

class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        
        ('Employee information', {'fields': ['first_name','last_name','company','email','phone']})
    ]
  
    list_display = ('first_name', 'last_name', 'company', 'email', 'phone')
    list_filter = ['company']

    search_fields = ['first_name']
    list_per_page = 10


admin.site.register(Company, CompanyAdmin)

admin.site.register(Employee, EmployeeAdmin)