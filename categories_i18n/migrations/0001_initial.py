# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import categories_i18n.abstract_models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='Parent', blank=True, to='categories_i18n.Category', on_delete=models.CASCADE, null=True)),
                ('site', models.ForeignKey(default=categories_i18n.abstract_models._get_current_site, blank=True, editable=False, to='sites.Site', on_delete=models.CASCADE, null=True)),
            ],
            options={
                'ordering': ('tree_id', 'lft'),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text='The slug is used in the URL of the page', max_length=100, verbose_name='slug')),
                ('master', models.ForeignKey(related_name='translations', to='categories_i18n.Category', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Category Translation',
                'verbose_name_plural': 'Category Translations',
            },
        ),
    ]
