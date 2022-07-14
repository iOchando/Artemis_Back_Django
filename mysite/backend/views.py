from tokenize import String
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets,status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser,IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
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
    filterset_fields = ('test', 'question', 'tipo')

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset=Answer.objects.all()
    serializer_class=AnswerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'answer')

@api_view(["POST"])
@csrf_exempt
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def guardar_certificacion(request):
    datos=request.data
    try:
        instructor=Profile.objects.get(id=datos['id'])
        test=Test.objects.create(instructor=instructor,course=datos['course_id'], score_approve=datos['score_approve'])
        
        for item in datos['certificacion']:
            question=Question.objects.create(test=test,pregunta=item['pregunta'],tipo=item['tipo'])
            if (item['tipo'] == 'simple'):
                for itemsimple in item['options']['simple']:
                    Answer.objects.create(question=question,respuesta=itemsimple['respuesta'],correcta=itemsimple['correcta'])
            else:
                for itemvof in item['options']['verdaderoFalso']:
                    Answer.objects.create(question=question,respuesta=itemvof['respuesta'],correcta=itemvof['correcta'])
    
        return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response('%s'%(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def get_certificacion(request):
    datos=request.data
    try:
        test=Test.objects.get(course=datos['course_id'])
        questions=Question.objects.filter(test=test)
        data = []
        i = 0
        for question in questions:
            answers=Answer.objects.filter(question=question)
            options = []
            for answer in answers:
                json = {
                    "option": answer.respuesta,
                    "isSelected": False
                }
                options.append(json)

            item = {
                "question": question.pregunta,
                "options": options
            }
            data.append(item)
    
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('%s'%(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
def revision_certificacion(request):
    datos=request.data
    print(datos)
    try:
        test=Test.objects.get(course=datos['course_id'])
        questions=Question.objects.filter(test=test)
        data = []
        for question in questions:
            answers=Answer.objects.filter(question=question)
            options = []
            for answer in answers:
                #json = {}
                #respuesta = ''
                if (answer.correcta == True):
                    respuesta = answer.respuesta
                    # json = {
                    #     "option": answer.respuesta,
                    #     "correcta": answer.correcta
                    # }                
                    # options.append(json)
                    item = {
                        "question": question.pregunta,
                        "respuesta": respuesta,
                    }
                    data.append(item)
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response('%s'%(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)