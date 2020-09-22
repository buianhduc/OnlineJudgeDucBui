# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-06 09:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', utils.models.RichTextField()),
                ('input_description', utils.models.RichTextField()),
                ('output_description', utils.models.RichTextField()),
                ('samples', jsonfield.fields.JSONField()),
                ('test_case_id', models.CharField(max_length=32)),
                ('test_case_score', jsonfield.fields.JSONField()),
                ('hint', utils.models.RichTextField(blank=True, null=True)),
                ('languages', jsonfield.fields.JSONField()),
                ('template', jsonfield.fields.JSONField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(blank=True, null=True)),
                ('time_limit', models.IntegerField()),
                ('memory_limit', models.IntegerField()),
                ('spj', models.BooleanField(default=False)),
                ('spj_language', models.CharField(blank=True, max_length=32, null=True)),
                ('spj_code', models.TextField(blank=True, null=True)),
                ('spj_version', models.CharField(blank=True, max_length=32, null=True)),
                ('rule_type', models.CharField(max_length=32)),
                ('visible', models.BooleanField(default=True)),
                ('difficulty', models.CharField(max_length=32)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('total_submit_number', models.IntegerField(default=0)),
                ('total_accepted_number', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'problem',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'problem_tag',
            },
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(to='problem.ProblemTag'),
        ),
    ]