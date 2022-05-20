from cgi import test
from django.db import models

# Create your models here.

class Profile(models.Model):
    wallet=models.CharField(max_length=255,unique=True ,null=False,blank=False)
    name=models.CharField(max_length=255,null=False,blank=False)
    last_name=models.CharField(max_length=255,null=False,blank=False)
    dni=models.CharField(unique=True, max_length=255,null=False,blank=False)
    email=models.EmailField(null=False,blank=True,default='')
    discord=models.CharField(max_length=255,null=False,blank=True,default='')
    profession=models.CharField(max_length=255,null=False,blank=True, default="")
    biography=models.TextField(null=False,blank=True,default='')
    country=models.CharField(max_length=255, null=False,blank=True,default='')
    def __str__(self):
        return self.wallet

class Test(models.Model):
    instructor=models.ForeignKey(Profile,null=False,on_delete=models.CASCADE)
    course=models.IntegerField(unique=True, null=False,blank=False)
    score_approve=models.FloatField(null=False, blank=True)
    def __str__(self):
        return self.course

class Question(models.Model):
    test=models.ForeignKey(Test,null=False,on_delete=models.CASCADE)
    question=models.CharField(max_length=255,unique=True ,null=False,blank=False)
    tipo=models.IntegerField(null=False,blank=False)
    score=models.FloatField(null=False, blank=True)
    def __str__(self):
        return self.test

class Answer(models.Model):
    question=models.ForeignKey(Question,null=False,on_delete=models.CASCADE)
    answer=models.CharField(max_length=255,unique=True ,null=False,blank=False)
    correct=models.BooleanField(null=False, blank=True,default=False)
    def __str__(self):
        return self.question