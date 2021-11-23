"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import  views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]

# _explanation
# The dot means that we are importing views from the same directory as this file
# The variable app_name helps django to distinguish this file from others with the same name
# The urlpatterns is a list with pages that can be requested from the app