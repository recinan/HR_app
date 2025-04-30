from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes, schema
from rest_framework.schemas import AutoSchema
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ApplicationSerializer
from .models import Application
from drf_spectacular.utils import extend_schema, OpenApiExample
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

# @extend_schema(
#     request=ApplicationSerializer,
#     examples=[
#         OpenApiExample(
#             'Form data example',
#             value={
#                 'jobTitle': 'Software Engineer',
#                 'cvFilePath': 'mycv.pdf',
#                 'description': 'Applying for backend role'
#             },
#             request_only=True
#         )
#     ],
#     responses={201: ApplicationSerializer},
#     summary="Create"
# )

@swagger_auto_schema(
    method='post',
    request_body=ApplicationSerializer,  # ✨ Buraya dikkat!
    responses={201: ApplicationSerializer},
    operation_summary="Create Application",
)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_application(request):
    # if request.method == 'GET':
    #     serializer = ApplicationSerializer()
    #     return Response(serializer.data)
    serializer = ApplicationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET','PUT'])
@parser_classes([MultiPartParser, FormParser])
def update_application(request,pk):
    application = Application.objects.get(pk=pk)
    serializer = ApplicationSerializer(application, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@parser_classes([MultiPartParser, FormParser])
def delete_application(request, pk):
    application = Application.objects.get(pk=pk)
    application.delete()
    content = "application deleted"
    return Response(content,status=204)

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def view_application(request,pk):
    application = Application.objects.get(pk=pk)
    serializer = ApplicationSerializer(application)
    return Response(serializer.data)

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def view_all_applications(request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)