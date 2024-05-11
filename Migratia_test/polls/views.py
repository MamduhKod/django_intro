from django.shortcuts import HttpResponse, render
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list}
    return render(request,"polls/index.html", context)

def detail(request, question_id):
    return HttpResponse('Youre looking at a question %s.' % question_id)

def results(request, question_id):
    response = 'Youre looking at the results of question %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('Youre voting on question %s.' % question_id)


