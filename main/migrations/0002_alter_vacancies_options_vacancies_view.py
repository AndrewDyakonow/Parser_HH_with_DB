# Generated by Django 4.2.4 on 2023-09-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancies',
            options={'ordering': ['-date_created'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AddField(
            model_name='vacancies',
            name='view',
            field=models.BooleanField(default=False, verbose_name='Признак просмотра'),
        ),
    ]
