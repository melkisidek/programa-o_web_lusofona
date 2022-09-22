from distutils.command import upload
from operator import mod
from pickle import TRUE
from turtle import mode, setx
from unicodedata import name
from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

class Post(models.Model):
    autor = models.CharField(max_length= 100)
    data = models.DateField()
    titulo = models.CharField(max_length= 300)
    descricao = models.TextField()
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.titulo[:50]


class Professor(models.Model):
   nome = models.CharField(max_length=50)
   Apelido = models.CharField(max_length=50)
   link_pagina_lusofona = models.URLField()
   linkedin = models.URLField()
   five_star_rate = models.FloatField

   def __str__(self):
      return self.nome + ' ' + self.Apelido


class Aluno(models.Model):
   nome = models.CharField(max_length=50)
   Apelido = models.CharField(max_length=50)
   link_pagina_lusofona = models.URLField()
   linkedin = models.URLField()

   def __str__(self):
      return self.nome + ' ' + self.Apelido


""""
class Projeto(models.Model):
    projeto = models.CharField(max_length=200)
    id_cadeiraFK = models.IntegerField()
    id_anoFK = models.IntegerField()
    topicofk = models.IntegerField()
    semestrefk = models.IntegerField()
    ano_frequentadoFk = models.IntegerField()
    descricao = models.TextField()
    linK_GitHuB = models.CharField(max_length=200)
    link_youtbe = models.CharField(max_length=200)
     
   """  





class Licenciatura(models.Model):
   licenciatura_nome = models.CharField(max_length=100)
  

   def __str__(self):
      return self.licenciatura_nome


class Cadeira(models.Model):
   cadeira_nome = models.CharField(max_length=20)
   ano = models.IntegerField()
   topico = models.TextField()
   semestre = models.SmallIntegerField()
   ano_frequentado = models.IntegerField()
   ects = models.SmallIntegerField()
   professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
   licenciatura = models.ManyToManyField(Licenciatura)
   
   def __str__(self):
      return self.cadeira_nome


class Tfc(models.Model):
   tfc_titulo = models.CharField(max_length=200)
   tfc_descricao = models.TextField(blank=TRUE)
   tfc_alunos = models.ForeignKey(Aluno, blank=TRUE, null=True, on_delete=models.CASCADE)
   orientador = models.ForeignKey(Professor, blank=TRUE, null=True, on_delete=models.CASCADE)
   tfc_licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE )
   
   def __str__(self):
      return self.tfc_titulo


class Pessoa(models.Model):
   LastName = models.CharField(max_length=50)
   FirstName = models.CharField(max_length=50)
   Gender = models.CharField(max_length=2)
   Age = models.IntegerField()

   #def __str__(self):
   #   return self.LastName


   class Friends(models.Model):
      name = models.CharField(max_length=50)
      age  = models.IntegerField()

