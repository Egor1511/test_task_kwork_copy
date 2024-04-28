# Generated by Django 5.0.4 on 2024-04-28 13:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Имя пользователя', max_length=50, null=True, verbose_name='Имя')),
                ('contact_info', models.TextField(blank=True, help_text='Контактная информация пользователя', null=True, verbose_name='Контактная информация')),
                ('experience', models.TextField(blank=True, help_text='Опыт работы пользователя', null=True, verbose_name='Опыт работы')),
                ('role', models.CharField(choices=[('CS', 'Заказчик'), ('FL', 'Фрилансер')], help_text='Роль пользователя', max_length=9, verbose_name='Роль')),
                ('user', models.OneToOneField(help_text='Пользователь', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FreelancerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Имя пользователя', max_length=50, null=True, verbose_name='Имя')),
                ('contact_info', models.TextField(blank=True, help_text='Контактная информация пользователя', null=True, verbose_name='Контактная информация')),
                ('experience', models.TextField(blank=True, help_text='Опыт работы пользователя', null=True, verbose_name='Опыт работы')),
                ('role', models.CharField(choices=[('CS', 'Заказчик'), ('FL', 'Фрилансер')], help_text='Роль пользователя', max_length=9, verbose_name='Роль')),
                ('user', models.OneToOneField(help_text='Пользователь', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Фрилансер',
                'verbose_name_plural': 'Фрилансеры',
                'ordering': ['name'],
            },
        ),
    ]
