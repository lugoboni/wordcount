from django import forms
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views.generic import View
from django.views.generic.edit import FormView

from .forms import (WordCountForm,)
from .models import (WordCount,)

class WordCountFormView(FormView):

    template_name = 'pages/word_count_form.html'
    form_class = WordCountForm
    initial = {}
    http_method_names = ['get', 'post', 'head', 'options', 'trace']

    def get(self, request):
        form = self.form_class()

        self.context = {'form': form}
        return render(request, self.template_name, self.context)

    def form_valid(self, form):
        try:
            with transaction.atomic():
                messages.success(self.request, "MLPAv4 saved")
                return redirect(self.request.META.get('PATH_INFO'))

        except ValidationError as e:
            messages.error(self.request, str(e))
            return redirect(self.request.META.get('PATH_INFO'))