from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.decorators import api_view, parser_classes, schema
from rest_framework.schemas import AutoSchema
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ApplicationSerializer
from .models import Application
from drf_spectacular.utils import extend_schema, OpenApiExample
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from users.decorators import role_required
import os
from django.shortcuts import get_object_or_404

# Create your views here.

@swagger_auto_schema(
    method='post',
    request_body=ApplicationSerializer,
    responses={201: ApplicationSerializer},
    operation_summary="Create Application",
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Candidate'])
def create_application(request):
    # if request.method == 'GET':
    #     serializer = ApplicationSerializer()
    #     return Response(serializer.data)
    serializer = ApplicationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@swagger_auto_schema(
    method='put',
    request_body=ApplicationSerializer,
    responses={200: ApplicationSerializer},
    operation_summary="Update Application",
)
@api_view(['GET','PUT'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Candidate'])
def update_application(request,pk):
    application = get_object_or_404(Application,pk=pk)
    if request.method == 'GET':
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ApplicationSerializer(application, data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Candidate'])
def delete_application(request, pk):
    application = get_object_or_404(Application,pk=pk)
    application.delete()
    content = "application deleted"
    return Response(content,status=204)

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Candidate','Evaulator'])
def view_application(request,pk):
    application = get_object_or_404(Application,pk=pk)
    serializer = ApplicationSerializer(application)
    return Response(serializer.data)

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Evaulator','Admin'])
def view_all_applications(request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def download_cv_file(request,pk):
    application = get_object_or_404(Application,pk=pk)
    cv_file_path = application.cvFilePath.path
    return FileResponse(open(cv_file_path,'rb'),as_attachment=True, filename=os.path.basename(cv_file_path))