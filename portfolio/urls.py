from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home_page_view, name='home'),
    path('apresentacao', views.apresentação_page_view, name='apresentacao'),
    path('competencias', views.competencias_page_view, name='competencias'),
    path('formacao', views.formação_page_view, name='formacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('cadeiras', views.cadeiras_page_view, name='cadeiras'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('highscores', views.highscores_page_view, name='highscores'),
    path('end', views.end_page_view, name='end'),

    path('tfc', views.tfc_page_view, name='tfc'),
    path('novo_tfc', views.novo_tfc_view, name='novo_tfc'),
    path('testcode', views.testcode_page_view, name='testcode'),

    path('sobre',views.sobre_page_view, name='sobre'),
    path('programacao_web',views.programacao_web_page_view, name='programacao_web'),
   
    path('blog',views.blog_page_view, name='blog'),
    path('novo/', views.novo_post_view, name='novo'),
    path('edita/<int:post_id>', views.edita_post_view, name='edita'),
    path('apaga/<int:post_id>', views.apaga_post_view, name='apaga'),

    path('projetoA',views.projetoA_page_view, name='projetoA'),
    path('projetoB',views.projetoB_page_view, name='projetoB'),
    path('projetoC',views.projetoC_page_view, name='projetoC'),
  
]