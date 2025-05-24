from django import forms

from .models import Post, Tag, Prof, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
            'author': forms.Select(),
        }

class TagModelForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'posts']
        widgets = {
            'name': forms.TextInput(),
            'posts': forms.CheckboxSelectMultiple(),
        }
        
class ProfModelForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = ['user', 'bio']
        widgets = {
            'user': forms.Select(),
            'bio': forms.Textarea(),
        }
        
class CommentModelForm(forms.ModelForm):  
    class Meta:
        model = Comment
        fields = ['post', 'author', 'text']
        widgets = {
            'post': forms.Select(),
            'author': forms.Select(),
            'text': forms.Textarea(attrs={'minlength': 10}),
        }