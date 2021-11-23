from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    """A form to accept a new topic adding."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """A form to accept a new entry adding."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}