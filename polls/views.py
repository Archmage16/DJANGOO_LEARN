from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions
from django.db.models import F
from django.core.paginator import Paginator


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
def question(req):
    if req.method == 'POST':
        text = req.POST.get('question_text')
        q1 = Question.objects.create(question_text=text)    
        q1.save()
        return render(req, 'polls/forms.html', {'question': q1})
    else:
        return render(req, 'polls/forms.html')
    
def choices(req):
    if req.method == 'POST':
        text = req.POST.get('choice_text')
        question_id = req.POST.get('question_id')
        # print(question_id)
        q1 = Question.objects.get(id=question_id)
        print(q1)
        c1 = Choice.objects.create(text_choice=text, question_text=q1)
        c1.save()
        return render(req, 'polls/choices.html', {'choice': c1})
    else:
        return render(req, 'polls/choices.html')
    
    
def paginator(req):
    ques = Question.objects.all()
    paginator = Paginator(ques, 3)
    page_number = req.GET.get('page')
    if page_number is None:
        page_number = 1
    if int(page_number) > int(paginator.num_pages):
        paginator = Paginator(ques, 13)
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(req, 'polls/paginator.html', context)

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
    