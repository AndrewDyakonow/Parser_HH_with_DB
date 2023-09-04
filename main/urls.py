from django.urls import path

from main.apps import MainConfig
from main.views import main_page, VacanciesListView, VacanciesDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', main_page, name='main_page'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies_list'),
    path('vacancies/<int:pk>/', VacanciesDetailView.as_view(), name='vacancy_detail'),
]
