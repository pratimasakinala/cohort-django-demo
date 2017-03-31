from django import forms
from .models import Comment

# class CommentForm(forms.Form):
#     name = Comment.name
#     comment = Comment.comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')
