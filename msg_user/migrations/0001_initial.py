# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=140, null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='messages',
            name='message_from',
            field=models.ForeignKey(related_name=b'message_from', to='msg_user.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='message_to',
            field=models.ForeignKey(related_name=b'message_to', to='msg_user.User'),
            preserve_default=True,
        ),
    ]
