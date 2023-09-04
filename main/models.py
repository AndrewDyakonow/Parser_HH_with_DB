from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Vacancies(models.Model):
    id_vacancy = models.PositiveIntegerField(unique=True, verbose_name='ID вакансии')
    name_company = models.CharField(max_length=127, verbose_name='Название компании')
    name_vacancy = models.CharField(max_length=127, verbose_name='Название вакансии')
    adress = models.CharField(max_length=255, **NULLABLE, verbose_name='Адрес')
    url = models.URLField(verbose_name='Ссылка на вакансию')
    salary_from = models.PositiveIntegerField(**NULLABLE, verbose_name='Зарплата от')
    salary_to = models.PositiveIntegerField(**NULLABLE, verbose_name='Зарплата до')
    requirement = models.TextField(max_length=1024, verbose_name='Требования')
    responsibiliti = models.TextField(max_length=1023, **NULLABLE, verbose_name='Ответственность')
    date_created = models.DateTimeField(verbose_name='Дата публикации')
    view = models.BooleanField(default=False, verbose_name='Признак просмотра')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.name_vacancy}, {self.salary_from}, {self.salary_to}'


# class Company(models.Model):
#     id_company = models.PositiveIntegerField(unique=True, verbose_name='ID вакансии')
#     name_company = models.CharField(max_length=127, verbose_name='Название компании')
#     url = models.URLField(verbose_name='Ссылка на компанию')
#     address = models.CharField(max_length=255, **NULLABLE, verbose_name='Адрес')
#
#     class Meta:
#         verbose_name = 'Компания'
#         verbose_name_plural = 'Компании'
#         ordering = ['name_company']
#
#     def __str__(self):
#         return f'{self.name_company}, {self.url}, {self.address}'
