from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    """A form to accept user input data."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}