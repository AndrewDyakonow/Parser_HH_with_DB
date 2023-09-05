# Generated by Django 4.2.4 on 2023-09-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_vacancies_requirement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancies',
            name='salary',
        ),
        migrations.AddField(
            model_name='vacancies',
            name='salary_from',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Зарплата от'),
        ),
        migrations.AddField(
            model_name='vacancies',
            name='salary_to',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Зарплата до'),
        ),
    ]