from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from main.forms import RequestForm
from main.models import Vacancies

from .utils.utils import requests


def main_page(request):
    request_form = RequestForm(request.POST)
    context = {'form': request_form}
    if request.method == 'POST':

        if request_form.is_valid():
            keyword = request_form.cleaned_data['keyword']
            requests(keyword)
            return HttpResponseRedirect(reverse('parser_pages:vacancies_list'))
        else:
            return render(request, 'main/main_page.html', context)
    else:
        return render(request, 'main/main_page.html', context)


class VacanciesListView(ListView):
    model = Vacancies
    queryset = Vacancies.objects.all()
    template_name = 'main/vacancies_list.html'
    paginate_by = 21


class VacanciesDetailView(DetailView):
    model = Vacancies
    template_name = 'main/vacancy_detail.html'

    def get_object(self, queryset=None):
        objects = super().get_object()
        objects.view = True
        objects.save()
        return objects

