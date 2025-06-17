from django import forms

from .models import Question, Choice

class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question', max_length=200)
class QuestionModelform(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.TextInput(),
        }


class ChoiceForm(forms.Form):
    question_text = forms.ModelChoiceField(queryset=Question.objects.all(), label='question')
    text_choice = forms.CharField(label='choice text', max_length=200)
    votes = forms.IntegerField(label='votes', initial=0, min_value=0)
    
    
class ChoiceModelform(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['question_text', 'text_choice', 'votes']
        widgets = {
            'question_text': forms.Select(),
            'text_choice': forms.TextInput(),
            'votes': forms.NumberInput(),
        }
    