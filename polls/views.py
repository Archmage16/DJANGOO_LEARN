from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions
from django.db.models import F
from django.core.paginator import Paginator


from polls.models import Question, Choice
from polls.forms import QuestionForm
from polls.forms import QuestionModelform
# from polls.forms import ChoiceForm
from polls.forms import ChoiceModelform


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
        form = QuestionModelform(req.POST)
        if form.is_valid():
            # question_text = form.cleaned_data['question_text']
            # question = Question.objects.create(question_text=question_text)
            form.save()
            return render(req, 'polls/forms.html', {'form': form})
        else:
            error = form.errors
            return render(req, 'polls/forms.html', {'error': error})
    else:
        form = QuestionForm()
        return render(req, 'polls/forms.html', {'form': form})
    
# def choices(req):
#     if req.method == 'POST':
#         form = ChoiceForm(req.POST)
#         if form.is_valid():
#             text_choice = form.cleaned_data['text_choice']
#             question_id = form.cleaned_data['question_id']
#             votes = form.cleaned_data['votes']
#             question = Question.objects.get(id=question_id)
#             if not question:
#                 return HttpResponse("Question not found")
#             choice = Choice.objects.create(text_choice=text_choice, question_text=question, votes=votes)
#             choice.save()
#             return render(req, 'polls/choices.html', {'form': form})
#         else:
#             error = form.errors
#             return render(req, 'polls/choices.html', {'error': error})
            
#     else:
#         form = ChoiceForm()
#         return render(req, 'polls/choices.html', {'form': form})
def choices(req):
    if req.method == 'POST':
        form = ChoiceModelform(req.POST)
        if form.is_valid():
            # choice = Choice.objects.create(**form.cleaned_data)
            form.save()
            return render(req, 'polls/choices.html', {'form': form})
        else:
            error = form.errors
            return render(req, 'polls/choices.html', {'error': error})
            
    else:
        form = ChoiceModelform()
        return render(req, 'polls/choices.html', {'form': form})   
    
    
    
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
    