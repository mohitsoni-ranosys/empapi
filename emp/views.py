from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Employee, Project, ProjectManagement
from .forms import EmployeeCreateForm, ProjectCreateForm, ProjectManagementForm
from .serializers import EmployeeSerializer, ProjectSerializer, UserSerializer


class EmployeeListView(View):
    template_name = 'employee_list.html'

    def get(self, request):
        all_employees = Employee.objects.all()
        return render(request, self.template_name,
                      {'employee_list': all_employees})


class EmployeeCreateView(View):
    template_name = 'employee_create.html'
    form_class = EmployeeCreateForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        if self.form_class(request.POST).is_valid():
            self.form_class(request.POST).save()
        else:
            print(self.form_class.errors)
        return render(request, self.template_name, {'form': self.form_class})


class EmployeeDetailView(View):
    template_name = 'employee_detail.html'

    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        return render(request, self.template_name, {'employee': employee})


class ProjectListView(View):
    template_name = 'project_list.html'

    def get(self, request):
        all_projects = Project.objects.all()
        return render(request, self.template_name, {'projects': all_projects})


class ProjectAddView(View):
    template_name = 'project_add.html'
    form_class = ProjectCreateForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        if self.form_class(request.POST).is_valid():
            self.form_class(request.POST).save()
        else:
            print(self.form_class.errors)
        return render(request, self.template_name, {'form': self.form_class})


class ProjectDetailView(View):
    template_name = 'project_detail.html'

    def get(self, request, pk):
        print("I am here")
        project_detail = ProjectManagement.objects.filter(Project=pk)
        print('***********************************')
        print(project_detail)
        print('***********************************')
        return render(request, self.template_name, {'project_detail': project_detail})


class ProjectAssignView(View):
    template_name = 'project_assign.html'
    form_class = ProjectManagementForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        if self.form_class(request.POST).is_valid():
            self.form_class(request.POST).save()
        else:
            print(self.form_class.errors)
        return render(request, self.template_name, {'form': self.form_class})

# Without serializers

# def emp_list(request):
#     if request.method == 'GET':
#         emp_list = Employee.objects.all()
#         print('+++++++++++++++++++++++++++++++')
#         print(emp_list.values('first_name', 'last_name', 'position', 'tech'))
#         data = {'employees': list(emp_list.values(
#             'first_name', 'last_name', 'position', 'tech'))}
#         return JsonResponse(data)


# with serializers

# 1. APIView
# class EmpList(APIView):
#     def get(self, request):
#         e_all = Employee.objects.all()
#         data = EmployeeSerializer(e_all, many=True).data
#         return Response(data)


# 2. Generic View
class EmpList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# without serializers

# def emp_detail(request, pk):
#     emp_obj = get_object_or_404(Employee, pk=pk)
#     data = {
#         'details': {
#             'first_name': emp_obj.first_name,
#             'last_name': emp_obj.last_name,
#             'position': emp_obj.position,
#             'tech': emp_obj.tech,
#         }
#     }
#     return JsonResponse(data)


# with serializer

# APIView
# class EmpDetail(APIView):
#     def get(self, request, pk):
#         e_obj = get_object_or_404(Employee, pk=pk)
#         data = EmployeeSerializer(e_obj).data
#         return Response(data)

# 2. Generic View

class EmpDetail(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)
