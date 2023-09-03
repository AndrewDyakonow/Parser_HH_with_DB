from django.db import models


class Vacancies(models.Model):
    id_vacancy = models.PositiveIntegerField(verbose_name='ID вакансии')
    name_company = models.ForeignKey('Company', on_delete=models.DO_NOTHING, verbose_name='Название компании')
    name_vacancy = models.CharField(max_length=127, verbose_name='Название вакансии')
    adress = models.CharField(max_length=255, verbose_name='Адрес')
    url = models.URLField(verbose_name='Ссылка на вакансию')
    salary = models.PositiveIntegerField(verbose_name='Зарплата')
    requirement = models.TextField(verbose_name='Требования')
    responsibiliti = models.TextField(max_length=1023, verbose_name='Ответственность')
    date_created = models.DateTimeField(verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['id_vacancy']

    def __str__(self):
        return f'{self.name_vacancy}, {self.salary}'


class Company(models.Model):
    id_company = models.PositiveIntegerField(verbose_name='ID вакансии')
    name_company = models.CharField(max_length=127, verbose_name='Название компании')
    url = models.URLField(verbose_name='Ссылка на компанию')
    adress = models.CharField(max_length=255, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['name_company']

    def __str__(self):
        return f'{self.name_company}'
