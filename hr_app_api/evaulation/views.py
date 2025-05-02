from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Evaulation
from .serializers import EvaulationSerializer, EvaulationCreateSerializer
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@swagger_auto_schema(
    method='post',
    request_body=EvaulationSerializer,
    responses={201: EvaulationSerializer},
    operation_summary='Create Evaulation'
)
@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser])
def create_evaulation(request):
    serializer = EvaulationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user_evaulator=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET','POST'])
@parser_classes([MultiPartParser,FormParser])
def update_evaulation(request):
    pass

@api_view(['DELETE'])
@parser_classes([MultiPartParser, FormParser])
def delete_evaulation(request):
    pass

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def view_evaulation(request, pk):
    pass

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
def view_all_evaulations(request):
    pass