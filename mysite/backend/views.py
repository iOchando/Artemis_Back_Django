from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets,status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('wallet', 'dni', 'name')

class TestViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset=Test.objects.all()
    serializer_class=TestSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('instructor', 'course', 'score_approve')

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('test', 'question', 'score')

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'answer')

@api_view(["POST"])
@csrf_exempt
@permission_classes(AllowAny)
def guardar_certificacion(request):
    datos=request.data
    try:
        instructor=Profile.objects.get(id=datos['id'])
        test=Test.objects.create(instructor=instructor,course=datos['course_id'], score_approve=datos['score_approve'])
        
        for item in datos['certificacion']:
            Question.objects.create(test=test,pregunta=item['pregunta'], tipo=item['tipo'])

        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response('%s'%(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
