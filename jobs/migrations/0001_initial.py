# Generated by Django 3.2.3 on 2021-05-28 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('logo', models.URLField(default='https://place-hold.it/100x60')),
                ('description', models.TextField()),
                ('employee_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('code', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('logo', models.URLField(default='https://place-hold.it/100x60')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('skills', models.TextField()),
                ('description', models.TextField()),
                ('salary_min', models.PositiveIntegerField()),
                ('salary_max', models.PositiveIntegerField()),
                ('published_at', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='vacancies', to='jobs.company')),
                ('speciality', models.ManyToManyField(related_name='vacancies', to='jobs.Speciality')),
            ],
        ),
    ]
