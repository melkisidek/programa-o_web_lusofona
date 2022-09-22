from http.client import HTTPResponse
import django
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

from django.urls import reverse

from .models import Post, Tfc

from .models import Pessoa

from .forms import PostForm, TfcForm
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin




######################################

class Pessoa:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido

    def __str__(self):
        return f"{self.nome} {self.apelido}"

P1 = Pessoa('melkisidek Pedro', 'Bequengue')

print(P1.nome + " "+P1.apelido)




class Aluno(Pessoa):
    def __init__(self,nome, apelido, link_pagina_lusofona, linkedin):
        super().__init__(nome, apelido)
        self.link_pagina_lusofona = link_pagina_lusofona
        self.linkedin = linkedin

    def __str__(self):
        return f"{self.nome} {self.apelido}{self.link_pagina_lusofona} {self.linkedin}"


AL1 = Aluno('Melkisidek Pedro','Bequengue', ' ','https://www.linkedin.com/in/lee-doo-hieng-9338b768/')
AL2 = Aluno('Carlos','Silva', ' ','https://www.linkedin.com/in/lee-doo-hieng-9338b768/')





class Professor(Pessoa):
    def __init__(self,nome, apelido, link_pagina_lusofona, linkedin):
        super().__init__(nome, apelido)
        self.link_pagina_lusofona = link_pagina_lusofona
        self.linkedin = linkedin

    def __str__(self):
        return f"{self.nome} {self.apelido}{self.link_pagina_lusofona} {self.linkedin}"

PR1 = Professor('Lee','Doo Hieng', ' ','https://www.linkedin.com/in/lee-doo-hieng-9338b768/')
PR2 = Professor('Lucio', ' Studer Ferreira', 'https://www.ulusofona.pt/teachers/lucio-miguel-studer-ferreira', 'https://www.linkedin.com/in/luciostuderferreira/')
PR3 = Professor('MARIA ', ' GONÇALVES COSTA', 'https://www.ulusofona.pt/teachers/maria-da-conceicao-goncalves-costa', '')

#######################################

################################################


class Cadeira:
    def __init__(self, cadeira, ano, topico,semestre, ano_frequentado, ects ):
        self.cadeira = cadeira
        self.ano = ano
        self.topico = topico
        self.semestre = semestre
        self.ano_frequentado = ano_frequentado
        self.ects = ects

    def __str__(self):
        return f"{self.cadeira} {self.ano}  {self.topico} {self.semestre} {self.ano_frequentado} {self.ects}"

contabilidade  = Cadeira('Contabilidade', 1 , 'A Contabilidade como Sistema de Informação. SNC Sistema de normalização. Elaboração das Demonstrações financeiras', 1, 2006,6 )
programaca_web = Cadeira('Programação Web', 2,'A Web e seus paradigmas.HTML e CSS para desenho de páginas Web.Python para desenvolvimento Web.Django web framework para Back-end',2,2006,6 )
marketing = Cadeira('Teoria e Prática de Marketing' , 1, ' Introdução ao Marketing. Segmentação, Targeting e Posicionamento.Objetivos e Estratégias de Marketing', 2 ,2022 ,6)

print(contabilidade)
print(programaca_web)
print(marketing)


class Projeto(Cadeira):
    def __init__(self, projeto, cadeira,  ano, topico,semestre, ano_frequentado, ects, descricao,linK_GitHuB,link_youtbe):
        super().__init__(cadeira, ano, topico,semestre, ano_frequentado, ects,)
        self.projeto = projeto
        self.descricao = descricao
        self.linK_GitHuB = linK_GitHuB
        self.link_youtbe = link_youtbe

    def __str__(self):
        return f"{self.projeto}{self.cadeira} {self.ano}  {self.topico} {self.semestre} {self.ano_frequentado} {self.ects} {self.descricao} {self.linK_GitHuB} {self.link_youtbe} "

PRJ1 = Projeto('Simulação Empresarial', 'Contabilidade', 1 , 'A Contabilidade como Sistema de Informação. SNC Sistema de normalização. Elaboração das Demonstrações financeiras', 1, 2006,6 , ' O objetivo da simulação empresarial ou jogos empresariais, é aprimorar conhecimentos de gestão por meio da simulação ', 'github.com', 'youtube.com')
PRJ2 = Projeto('Marketing Empresarial', 'Marketing', 1 , 'A Contabilidade como Sistema de Informação. SNC Sistema de normalização. Elaboração das Demonstrações financeiras', 1, 2006,6 , ' O Marketing Empresarial é um conjunto de ações promocionais que tem como objetivo conquistar novos clientes e fidelizar', 'github.com', 'youtube.com')
PRJ3 = Projeto('Portfolio web com Django', 'Progamação web', 1 , 'A Contabilidade como Sistema de Informação. SNC Sistema de normalização. Elaboração das Demonstrações financeiras', 1, 2006,6 , ' Realização um portfolio web usando a framewok django. Pragramação python css e javascript.', 'github.com', 'youtube.com')

print(PRJ1)
print(PRJ2)
print(PRJ3)
################################################
def index(request):
	return render(request, 'portfolio/index.html')

def home_page_view(request):
	return render(request, 'portfolio/home.html')


def apresentação_page_view(request):
	return render(request, 'portfolio/apresentação.html')


def competencias_page_view(request):
	return render(request, 'portfolio/competencias.html')


def formação_page_view(request):
	return render(request, 'portfolio/formação.html')

def projetos_page_view(request):
	return render(request, 'portfolio/projetos.html' , {
    'contabilidade_cadeira':contabilidade.cadeira,
    'contabilidade_ano':contabilidade.ano,
    'contabilidade_topico':contabilidade.topico,
    'contabilidade_semestre':contabilidade.semestre,
    'contabilidade_ano_frequentado':contabilidade.ano_frequentado,
    'contabilidade_ects':contabilidade.ects,

    'programaca_web_cadeira': programaca_web.cadeira,
    'programaca_web_ano': programaca_web.ano,
    'programaca_web_topico': programaca_web.topico,
    'programaca_web_semestre': programaca_web.semestre,
    'programaca_web_ano_frequentado': programaca_web.ano_frequentado,
    'programaca_web_ects': programaca_web.ects,

    'marketing_web_cadeira': marketing.cadeira,
    'marketing_web_ano': marketing.ano,
    'marketing_web_topico': marketing.topico,
    'marketing_web_semestre': marketing.semestre,
    'marketing_web_ano_frequentado': marketing.ano_frequentado,
    'marketing_web_ects': marketing.ects,

    'Aluno_AL1_nome': AL1.nome,
    'Aluno_AL1_apelido': AL1.apelido,
    'Aluno_AL1_link_pagina_lusofona': AL1.link_pagina_lusofona,
    'Aluno_AL1_linkedin': AL1.linkedin,

    'Aluno_AL2_nome': AL2.nome,
    'Aluno_AL2_apelido': AL2.apelido,
    'Aluno_AL2_link_pagina_lusofona': AL2.link_pagina_lusofona,
    'Aluno_AL2_linkedin': AL2.linkedin,

    

    'professor_PR1_nome': PR1.nome,
    'professor_PR1_apelido': PR1.apelido,
    'professor_PR1_link_pagina_lusofona': PR1.link_pagina_lusofona,
    'professor_PR1_linkedin': PR1.linkedin,

    'professor_PR2': PR2.nome,
    'professor_PR2': PR2.apelido,
    'professor_PR2': PR2.link_pagina_lusofona,
    'professor_PR2': PR2.linkedin,

    'professor_PR3': PR3.nome,
    'professor_PR3': PR3.apelido,
    'professor_PR3': PR3.link_pagina_lusofona,
    'professor_PR3': PR3.linkedin,



    'projeto_PRJ1_projeto': PRJ1.projeto,
    'projeto_PRJ1_cadeira': PRJ1.cadeira,
    'projeto_PRJ1_topico': PRJ1.topico,
    'projeto_PRJ1_semestre': PRJ1.semestre,
    'projeto_PRJ1_ano_frequentado': PRJ1.ano_frequentado,
    'projeto_PRJ1_ects': PRJ1.ects,
    'projeto_PRJ1_descricao': PRJ1.descricao,
    'projeto_PRJ1_linK_GitHuB': PRJ1.linK_GitHuB,
    'projeto_PRJ1_link_youtbe': PRJ1.link_youtbe,


    'projeto_PRJ2_projeto': PRJ2.projeto,
    'projeto_PRJ2_cadeira': PRJ2.cadeira,
    'projeto_PRJ2_topico': PRJ2.topico,
    'projeto_PRJ2_semestre': PRJ2.semestre,
    'projeto_PRJ2_frequentado': PRJ2.ano_frequentado,
    'projeto_PRJ2_ects': PRJ2.ects,
    'projeto_PRJ2_descricao': PRJ2.descricao,
    'projeto_PRJ2_linK_GitHuB': PRJ2.linK_GitHuB,
    'projeto_PRJ2_link_youtbe': PRJ2.link_youtbe,


    'projeto_PRJ3_projeto': PRJ3.projeto,
    'projeto_PRJ3_cadeira': PRJ3.cadeira,
    'projeto_PRJ3_topico': PRJ3.topico,
    'projeto_PRJ3_semestre': PRJ3.semestre,
    'projeto_PRJ3_frequentado': PRJ3.ano_frequentado,
    'projeto_PRJ3_ects': PRJ3.ects,
    'projeto_PRJ3_descricao': PRJ3.descricao,
    'projeto_PRJ3_linK_GitHuB': PRJ3.linK_GitHuB,
    'projeto_PRJ3_link_youtbe': PRJ3.link_youtbe,
    
    })


def licenciatura_page_view(request):
	return render(request, 'portfolio/licenciatura.html', {
    'contabilidade_cadeira':contabilidade.cadeira,
    'contabilidade_ano':contabilidade.ano,
    'contabilidade_topico':contabilidade.topico,
    'contabilidade_semestre':contabilidade.semestre,
    'contabilidade_ano_frequentado':contabilidade.ano_frequentado,
    'contabilidade_ects':contabilidade.ects,

    'programaca_web_cadeira': programaca_web.cadeira,
    'programaca_web_ano': programaca_web.ano,
    'programaca_web_topico': programaca_web.topico,
    'programaca_web_semestre': programaca_web.semestre,
    'programaca_web_ano_frequentado': programaca_web.ano_frequentado,
    'programaca_web_ects': programaca_web.ects,

    'marketing_cadeira': marketing.cadeira,
    'marketing_ano': marketing.ano,
    'marketing_topico': marketing.topico,
    'marketing_semestre': marketing.semestre,
    'marketing_ano_frequentado': marketing.ano_frequentado,
    'marketing_ects': marketing.ects,

    'professor_PR1_nome': PR1.nome,
    'professor_PR1_apelido': PR1.apelido,
    'professor_PR1_link_pagina_lusofona': PR1.link_pagina_lusofona,
    'professor_PR1_linkedin': PR1.linkedin,

    'professor_PR2_nome': PR2.nome,
    'professor_PR2_apelido': PR2.apelido,
    'professor_PR2_link_pagina_lusofona': PR2.link_pagina_lusofona,
    'professor_PR2_linkedin': PR2.linkedin,

    'professor_PR3_nome': PR3.nome,
    'professor_PR3_apelido': PR3.apelido,
    'professor_PR3_link_pagina_lusofona': PR3.link_pagina_lusofona,
    'professor_PR3_linkedin': PR3.linkedin,


    'projeto_PRJ1_projeto': PRJ1.projeto,
    'projeto_PRJ1_cadeira': PRJ1.cadeira,
    'projeto_PRJ1_topico': PRJ1.topico,
    'projeto_PRJ1_semestre': PRJ1.semestre,
    'projeto_PRJ1_ano_frequentado': PRJ1.ano_frequentado,
    'projeto_PRJ1_ects': PRJ1.ects,
    'projeto_PRJ1_descricao': PRJ1.descricao,
    'projeto_PRJ1_linK_GitHuB': PRJ1.linK_GitHuB,
    'projeto_PRJ1_link_youtbe': PRJ1.link_youtbe,


    'projeto_PRJ2_projeto': PRJ2.projeto,
    'projeto_PRJ2_cadeira': PRJ2.cadeira,
    'projeto_PRJ2_topico': PRJ2.topico,
    'projeto_PRJ2_semestre': PRJ2.semestre,
    'projeto_PRJ2_frequentado': PRJ2.ano_frequentado,
    'projeto_PRJ2_ects': PRJ2.ects,
    'projeto_PRJ2_descricao': PRJ2.descricao,
    'projeto_PRJ2_linK_GitHuB': PRJ2.linK_GitHuB,
    'projeto_PRJ2_link_youtbe': PRJ2.link_youtbe,


    'projeto_PRJ3_projeto': PRJ3.projeto,
    'projeto_PRJ3_cadeira': PRJ3.cadeira,
    'projeto_PRJ3_topico': PRJ3.topico,
    'projeto_PRJ3_semestre': PRJ3.semestre,
    'projeto_PRJ3_frequentado': PRJ3.ano_frequentado,
    'projeto_PRJ3_ects': PRJ3.ects,
    'projeto_PRJ3_descricao': PRJ3.descricao,
    'projeto_PRJ3_linK_GitHuB': PRJ3.linK_GitHuB,
    'projeto_PRJ3_link_youtbe': PRJ3.link_youtbe,
   


    })
  

def cadeiras_page_view(request):
	return render(request, 'portfolio/cadeiras.html')



def index_view(request):
    return render(request, 'portfolio/index.html', {'nome':P1.nome,'apelido': P1.apelido})


from datetime import date, datetime 

class Pessoa:
    def __init__(self, nome, linkedin):
        self.nome = nome
        self.linkedin = linkedin

    def __str__(self):
        return f"{self.nome} {self.linkedin}"

print(Pessoa('Melkisidek Pedro Bequengue', 'melkisidek@linkedin.com'))


class Competencia:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"

print(Competencia('html'))


class Pessoa:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido

    def __str__(self):
        return f"{self.nome} {self.apelido}"

P1 = Pessoa('melkisidek Pedro', 'Bequengue')

print(P1.nome + " "+P1.apelido)



def blog_page_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', context)


def novo_post_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/novo.html', context)


def edita_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_post_view(request, post_id):
    Post.objects.get(id=post_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))


def quiz_page_view(request):
    return render(request,'portfolio/quiz.html')

def testcode_page_view(request):
   
    pessoas = Pessoa.objects.all()
    context = {'pessoas':pessoas}
    return render(request, 'portfolio/testcode.html', context)


def highscores_page_view(request):
    return render(request,'portfolio/highscores.html')

def end_page_view(request):
    return render(request,'portfolio/end.html')

def tfc_page_view(request):
    context ={'tfcs':Tfc.objects.all()}
    return render(request,'portfolio/tfc.html',context)


def novo_tfc_view(request):
    data = Tfc.objects.all()
    form = TfcForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:novo_tfc'))

    context = {'form': form,'data':data}
    
    return render(request, 'portfolio/novo_TFC.html', context)


def sobre_page_view(request):
    
    return render(request,'portfolio/sobre.html')


def programacao_web_page_view(request):
    
    return render(request,'portfolio/programacao_web.html')


def projetoA_page_view(request):
   return render(request,'portfolio/projetoA.html',{'projeto_PRJ1_projeto': PRJ1.projeto,
    'projeto_PRJ1_cadeira': PRJ1.cadeira,
    'projeto_PRJ1_topico': PRJ1.topico,
    'projeto_PRJ1_semestre': PRJ1.semestre,
    'projeto_PRJ1_ano_frequentado': PRJ1.ano_frequentado,
    'projeto_PRJ1_ects': PRJ1.ects,
    'projeto_PRJ1_descricao': PRJ1.descricao,
    'projeto_PRJ1_linK_GitHuB': PRJ1.linK_GitHuB,
    'projeto_PRJ1_link_youtbe': PRJ1.link_youtbe,
})

def projetoB_page_view(request):
   return render(request,'portfolio/projetoB.html',{
   
    'projeto_PRJ2_projeto': PRJ2.projeto,
    'projeto_PRJ2_cadeira': PRJ2.cadeira,
    'projeto_PRJ2_topico': PRJ2.topico,
    'projeto_PRJ2_semestre': PRJ2.semestre,
    'projeto_PRJ2_frequentado': PRJ2.ano_frequentado,
    'projeto_PRJ2_ects': PRJ2.ects,
    'projeto_PRJ2_descricao': PRJ2.descricao,
    'projeto_PRJ2_linK_GitHuB': PRJ2.linK_GitHuB,
    'projeto_PRJ2_link_youtbe': PRJ2.link_youtbe,


  })

def projetoC_page_view(request):
   return render(request,'portfolio/projetoC.html',{
    'projeto_PRJ3_projeto': PRJ3.projeto,
    'projeto_PRJ3_cadeira': PRJ3.cadeira,
    'projeto_PRJ3_topico': PRJ3.topico,
    'projeto_PRJ3_semestre': PRJ3.semestre,
    'projeto_PRJ3_frequentado': PRJ3.ano_frequentado,
    'projeto_PRJ3_ects': PRJ3.ects,
    'projeto_PRJ3_descricao': PRJ3.descricao,
    'projeto_PRJ3_linK_GitHuB': PRJ3.linK_GitHuB,
    'projeto_PRJ3_link_youtbe': PRJ3.link_youtbe,})



@xframe_options_sameorigin
def home(request):
    return render(request, 'newapp/home.html')


