from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status



class IndexView(TemplateView):
    template_name = "index.html"

class ReactView(TemplateView):
    template_name = "react_app.html"

#
# class employee_details(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     permission_classes = (permissions.IsAuthenticated,)

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    This viewset provide list , create actions.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

# @api_view(['GET', 'POST'])
# def EmployeeViewSet(request):
#     """
#     List all snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Employee.objects.all()
#         serializer = EmployeeSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # def EmployeeViewSet(request, format=None):