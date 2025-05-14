from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions
from django.db.models import F


from polls.models import Question, Choice


# Create your views here.
def index(req):
    ques = Question.objects.all()
    cont = {'questions': ques, 'mess':"Hi boss!", 'showMess': False,
            "prod": [
                {"name":'Apple', "price": 500},
                {"name":'Macaroni', "price": 400},
                {"name":'Milk', "price": 700},
            ]}
    # return render(req,'polls/index.html', cont)
    return render(req,'polls/in.html', cont)

def detail(req, question_id):
    # try:
    #     objecst = Question.objects.get(id = question_id)
    #     return HttpResponse(objecst)
    # except exceptions.ObjectDoesNotExist:
    #     return HttpResponse("Sorry we don't have this odject")
    objectt = Question.objects.filter(id=question_id).first()
    ans = Choice.objects.filter(question_text_id = question_id).first()
    if objectt and ans:
        return HttpResponse(f"{objectt} <br>{ans} votes")
    return HttpResponse("Sorry we don't have this quesiton or ans")

def votes(req, choice_id):
    choice = Choice.objects.filter(id=choice_id)
    if choice:
        choice.update(votes = F("votes") + 1)
        return HttpResponse(choice)
    return HttpResponse("Can't fint this choice")
    