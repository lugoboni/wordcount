from django import forms
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views.generic import View
from django.contrib import messages

from django.views.generic.edit import FormView

from .forms import (WordCountForm,)
# from .models import (WordCount,)
from .use_cases import count_words_use_case

NO_WORDS_MESSAGE = "Please, type some words before submit"
COUNT_RESULT_MESSAGE = "The typed text has {} counted words"
UNKNOW_ERROR = "Something's wrong"

class WordCountFormView(FormView):

    template_name = 'pages/word_count_form.html'
    form_class = WordCountForm
    initial = {}
    http_method_names = ['get', 'post', 'head', 'options', 'trace']

    def get(self, request):
        form = self.form_class()

        self.context = {'form': form}
        return render(request, self.template_name, self.context)

    def form_invalid(self, form):
        messages.error(self.request, UNKNOW_ERROR)
        return redirect(self.request.META.get('PATH_INFO'))

    def form_valid(self, form):
        
        form_data = form.cleaned_data

        words_to_count = form_data['words']
        words_number = count_words_use_case(words_to_count)

        if words_number == 0:
            messages.warning(self.request, NO_WORDS_MESSAGE)
        else:
            messages.success(self.request, COUNT_RESULT_MESSAGE.format(words_number))
        
        return redirect(self.request.META.get('PATH_INFO'))