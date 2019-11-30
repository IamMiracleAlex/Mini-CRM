from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee
from .serializers import EmployeeSerializer

# class EmployeeView(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         # the many param informs the serializer that it will be serializing more than a single employee
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response({"employees": serializer.data})

#     def post(self, request):
#         employee = request.data.get('employee')

#         # Create an employee from the above data
#         serializer = EmployeeSerializer(data=employee)
#         if serializer.is_valid(raise_exception=True):
#             employee_saved = serializer.save()
#         return Response({"success": f"Employee {employee_saved.first_name} created successfully"})    


from rest_framework import viewsets          
from .serializers import EmployeeSerializer      
from .models import Employee                    
        
class EmployeeView(viewsets.ModelViewSet):       
  serializer_class = EmployeeSerializer          
  queryset = Employee.objects.all() 