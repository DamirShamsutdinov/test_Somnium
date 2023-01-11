# Generated by Django 4.1.5 on 2023-01-10 14:06

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название департамента')),
                ('description', models.TextField(verbose_name='Описание департамента')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название штатки')),
                ('salary', models.PositiveSmallIntegerField(verbose_name='Заработная плата')),
                ('description', models.TextField(verbose_name='Обязанности и т.п.')),
                ('department', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dep_position', to='departments.department', verbose_name='Департамент')),
            ],
            options={
                'verbose_name': 'Позиция в штатке',
                'db_table': 'position',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], max_length=1, verbose_name='Половой признак')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='position_spec', to='departments.position', verbose_name='Позиция в штатке')),
            ],
            options={
                'verbose_name': 'Специалист',
                'verbose_name_plural': 'Специалисты',
                'db_table': 'specialist',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='department',
            name='boss',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dep_boss', to='departments.specialist', verbose_name='Босс департамента'),
        ),
        migrations.AddField(
            model_name='department',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='departments.department'),
        ),
        migrations.AddField(
            model_name='department',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='dep_staff', to='departments.specialist', verbose_name='Штатный сотрудник департамента'),
        ),
    ]
