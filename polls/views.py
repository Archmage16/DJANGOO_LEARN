from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions
from django.db.models import F
from django.core.paginator import Paginator
from django.views import View
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


from polls.models import Question, Choice
from polls.forms import QuestionForm
from polls.forms import QuestionModelform
# from polls.forms import ChoiceForm
from polls.forms import ChoiceModelform

# Create your views here.
def index(req):
    ques = Question.objects.all()
    cont = {'questions': ques, 'mess':"Hi boss!", 'showMess': False,}
    # return render(req,'polls/index.html', cont)
    return render(req,'polls/in.html', cont) 

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/in.html'
    context_object_name = 'questions'
    paginate_by = 1
    
class IndexView(TemplateView):
    template_name = 'polls/ques/paginator.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context
    pass   



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
    
class AddQues(FormView):
    template_name = "polls/forms.html"
    form_class = QuestionModelform
    success_url = 'question-suc/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class QuesSuc(View):
    def get(self, req):
        return render(req, 'polls/ques/question-suc.html')

class ChoiceSuc(View):
    def get(self, req):
        return render(req, 'polls/choices/choice-suc.html')
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
            return render(req, 'polls/choices/choices.html', {'form': form})
        else:
            error = form.errors
            return render(req, 'polls/choices/choices.html', {'error': error})
            
    else:
        form = ChoiceModelform()
        return render(req, 'polls/choices/choices.html', {'form': form})   
    
    
    
# def paginator(req):
#     ques = Question.objects.all()
#     paginator = Paginator(ques, 3)
#     page_number = req.GET.get('page')
#     if page_number is None:
#         page_number = 1
#     if int(page_number) > int(paginator.num_pages):
#         paginator = Paginator(ques, 13)
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj': page_obj,
#         'paginator': paginator,
#     }
#     return render(req, 'polls/paginator.html', context)



# class ChoiceListView(ListView):
#     model = Choice
#     template_name = 'polls/pagiCH.html'
#     context_object_name = 'choices'
#     paginate_by = 5
#     def get_queryset(self):
#         question_id = self.kwargs.get('question_id')
#         return Choice.objects.filter(question_text_id = question_id)  
#     pass


# def detail(req, question_id):
#     try:
#         objecst = Question.objects.get(id = question_id)
#         return HttpResponse(objecst)
#     except exceptions.ObjectDoesNotExist:
#         return HttpResponse("Sorry we don't have this odject")
    

# class PollsDetailView(View):
#     http_method_names = ['get']

#     def get(self, req, question_id):
#         objectt = Question.objects.filter(id=question_id).first()
#         ans = Choice.objects.filter(question_text_id = question_id).first()
#         if objectt and ans:
#             return HttpResponse(f"{objectt} <br>{ans}")
#         return HttpResponse("Sorry we don't have this quesiton or ans")

class QuesDetailView(DetailView):
    model = Question
    pk_url_kwarg = 'question_id' 
    template_name = 'polls/ques/question_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ques = self.kwargs
        context['ch'] = Choice.objects.filter(question_text_id = ques['question_id'])
        return context

class QuesCreateeView(CreateView):
    model = Question
    fields = ['question_text']    
    template_name = 'polls/ques/formQues.html'
    success_url = reverse_lazy('polls:question-suc')
class QuesUpdateView(UpdateView):
    model = Question
    fields = ['question_text']
    pk_url_kwarg = 'question_id'
    template_name = 'polls/ques/formQues.html'
    success_url = reverse_lazy('polls:question-suc')
class QuesDeleteView(DeleteView):
    model = Question
    template_name = 'polls/ques/formQues.html'
    pk_url_kwarg = 'question_id'
    success_url = reverse_lazy('polls:question-suc')


class ChoiceCreateeView(CreateView):
    model = Choice
    form_class = ChoiceModelform
    success_url = reverse_lazy('polls:choice-suc')
    template_name = 'polls/ques/formQues.html'
    def form_valid(self, form):
        question_id = self.kwargs.get('question_text_id')
        form.instance.question_id = question_id
        return super().form_valid(form)
class ChoiceUpdateView(UpdateView):
    model = Choice
    fields = ['text_choice']
    pk_url_kwarg = 'question_text_id'

    template_name = 'polls/ques/formQues.html'
    success_url = reverse_lazy('polls:choice-suc')
class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'polls/ques/formQues.html'
    pk_url_kwarg = 'question_text_id'
    success_url = reverse_lazy('polls:choice-suc')





def votes(req, choice_id):
    choice = Choice.objects.filter(id=choice_id)
    if choice:
        choice.update(votes = F("votes") + 1)
        return HttpResponse(choice)
    return HttpResponse("Can't fint this choice")

class Greet(View):
    greet = "HI"
    def get(self, req):
        return HttpResponse(self.greet)

class TeacherGreet(Greet):
    greet = "Hi teacher"

class StudentGreet(Greet):
    greet = "Hi Student"