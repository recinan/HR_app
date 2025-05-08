from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Evaulation
from users.models import Role
from .serializers import EvaulationSerializer, EvaulationCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from users.decorators import role_required
from django.shortcuts import get_object_or_404
from .permissions import IsAdmin


# Create your views here.

@swagger_auto_schema(
    method='post',
    request_body=EvaulationSerializer,
    responses={201: EvaulationSerializer},
    operation_summary='Create Evaulation'
)
@api_view(['POST'])
@parser_classes([MultiPartParser,FormParser])
@role_required(['Evaluator','Admin'])
def create_evaulation(request):
    serializer = EvaulationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user_evaulator=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@swagger_auto_schema(
    method='put',
    request_body=EvaulationSerializer,
    responses={201: EvaulationSerializer},
    operation_summary='Update Evaulation'
)
@api_view(['PUT'])
@parser_classes([MultiPartParser,FormParser])
@role_required(['Evaluator','Admin'])
def update_evaulation(request,pk):
    evaulation = get_object_or_404(Evaulation, pk=pk)
    serializer = EvaulationSerializer(evaulation, data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Evaluator','Admin'])
def delete_evaulation(request,pk):
    evaulation = get_object_or_404(Evaulation, pk=pk)
    evaulation.delete()
    return Response(status=204)

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Evaluator','Admin','Candidate'])
def view_evaulation(request, pk):
    evaluation = get_object_or_404(Evaulation, pk=pk)

    if request.user.user_role in ['Evaluator','Admin']:
        serializer = EvaulationSerializer(evaluation)
        return Response(serializer.data)
    
    elif request.user.user_role == 'Candidate':
        sum_of_evaluators = Role.objects.filter(role_name='Evaluator').count()
        sum_of_evaluations = Evaulation.objects.filter(application=evaluation.application).count()

        if sum_of_evaluators >= sum_of_evaluations:
            serializer = EvaulationSerializer(evaluation)
            return Response(serializer.data)
        else:
            return Response({'error':'This evaluation has not been completed'})
    else:
        return Response({'error':'You are not allowed to see this'})        

@api_view(['GET'])
@parser_classes([MultiPartParser, FormParser])
@role_required(['Admin'])
@permission_classes([IsAdmin])
def view_all_evaulations(request):
    evaulations = Evaulation.objects.all()

    if IsAdmin().has_object_permission(request, None, evaulations):
        return Response({"error":"You are not allowed to do this!"}, status=403)
    
    serializer = EvaulationSerializer(evaulations, many=True)
    return Response(serializer.data)