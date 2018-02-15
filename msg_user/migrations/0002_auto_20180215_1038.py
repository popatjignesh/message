# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=140, null=True, blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('message_from', models.ForeignKey(related_name=b'message_from', to='msg_user.User')),
                ('message_to', models.ForeignKey(related_name=b'message_to', to='msg_user.User')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Message',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='messages',
            name='message_from',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='message_to',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]
