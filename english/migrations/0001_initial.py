# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='database',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocabulary', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocabulary', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('vowel', models.CharField(max_length=20)),
                ('history', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='exercisescratch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic1', models.CharField(max_length=20)),
                ('topic2', models.CharField(max_length=20)),
                ('topic3', models.CharField(max_length=20)),
                ('topic4', models.CharField(max_length=20)),
                ('topic5', models.CharField(max_length=20)),
                ('topic6', models.CharField(max_length=20)),
                ('topic7', models.CharField(max_length=20)),
                ('topic8', models.CharField(max_length=20)),
                ('topic9', models.CharField(max_length=20)),
                ('topic10', models.CharField(max_length=20)),
                ('topic11', models.CharField(max_length=20)),
                ('topic12', models.CharField(max_length=20)),
                ('topic13', models.CharField(max_length=20)),
                ('topic14', models.CharField(max_length=20)),
                ('topic15', models.CharField(max_length=20)),
                ('topic16', models.CharField(max_length=20)),
                ('topic17', models.CharField(max_length=20)),
                ('topic18', models.CharField(max_length=20)),
                ('topic19', models.CharField(max_length=20)),
                ('topic20', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='kkdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=20, blank=True)),
                ('kk', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='phoneme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vowel', models.CharField(max_length=20)),
                ('packet', models.ForeignKey(to='english.group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='posttestscratch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic1', models.CharField(max_length=20)),
                ('topic2', models.CharField(max_length=20)),
                ('topic3', models.CharField(max_length=20)),
                ('topic4', models.CharField(max_length=20)),
                ('topic5', models.CharField(max_length=20)),
                ('topic6', models.CharField(max_length=20)),
                ('topic7', models.CharField(max_length=20)),
                ('topic8', models.CharField(max_length=20)),
                ('topic9', models.CharField(max_length=20)),
                ('topic10', models.CharField(max_length=20)),
                ('topic11', models.CharField(max_length=20)),
                ('topic12', models.CharField(max_length=20)),
                ('topic13', models.CharField(max_length=20)),
                ('topic14', models.CharField(max_length=20)),
                ('topic15', models.CharField(max_length=20)),
                ('topic16', models.CharField(max_length=20)),
                ('topic17', models.CharField(max_length=20)),
                ('topic18', models.CharField(max_length=20)),
                ('topic19', models.CharField(max_length=20)),
                ('topic20', models.CharField(max_length=20)),
                ('topic21', models.CharField(max_length=20)),
                ('topic22', models.CharField(max_length=20)),
                ('topic23', models.CharField(max_length=20)),
                ('topic24', models.CharField(max_length=20)),
                ('topic25', models.CharField(max_length=20)),
                ('topic26', models.CharField(max_length=20)),
                ('topic27', models.CharField(max_length=20)),
                ('topic28', models.CharField(max_length=20)),
                ('topic29', models.CharField(max_length=20)),
                ('topic30', models.CharField(max_length=20)),
                ('topic31', models.CharField(max_length=20)),
                ('topic32', models.CharField(max_length=20)),
                ('topic33', models.CharField(max_length=20)),
                ('topic34', models.CharField(max_length=20)),
                ('topic35', models.CharField(max_length=20)),
                ('topic36', models.CharField(max_length=20)),
                ('topic37', models.CharField(max_length=20)),
                ('topic38', models.CharField(max_length=20)),
                ('topic39', models.CharField(max_length=20)),
                ('topic40', models.CharField(max_length=20)),
                ('topic41', models.CharField(max_length=20)),
                ('topic42', models.CharField(max_length=20)),
                ('topic43', models.CharField(max_length=20)),
                ('topic44', models.CharField(max_length=20)),
                ('topic45', models.CharField(max_length=20)),
                ('topic46', models.CharField(max_length=20)),
                ('topic47', models.CharField(max_length=20)),
                ('topic48', models.CharField(max_length=20)),
                ('topic49', models.CharField(max_length=20)),
                ('topic50', models.CharField(max_length=20)),
                ('topic51', models.CharField(max_length=20)),
                ('topic52', models.CharField(max_length=20)),
                ('topic53', models.CharField(max_length=20)),
                ('topic54', models.CharField(max_length=20)),
                ('topic55', models.CharField(max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='posttestspeaking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocabulary', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('vowel', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pretestscratch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic1', models.CharField(max_length=20)),
                ('topic2', models.CharField(max_length=20)),
                ('topic3', models.CharField(max_length=20)),
                ('topic4', models.CharField(max_length=20)),
                ('topic5', models.CharField(max_length=20)),
                ('topic6', models.CharField(max_length=20)),
                ('topic7', models.CharField(max_length=20)),
                ('topic8', models.CharField(max_length=20)),
                ('topic9', models.CharField(max_length=20)),
                ('topic10', models.CharField(max_length=20)),
                ('topic11', models.CharField(max_length=20)),
                ('topic12', models.CharField(max_length=20)),
                ('topic13', models.CharField(max_length=20)),
                ('topic14', models.CharField(max_length=20)),
                ('topic15', models.CharField(max_length=20)),
                ('topic16', models.CharField(max_length=20)),
                ('topic17', models.CharField(max_length=20)),
                ('topic18', models.CharField(max_length=20)),
                ('topic19', models.CharField(max_length=20)),
                ('topic20', models.CharField(max_length=20)),
                ('topic21', models.CharField(max_length=20)),
                ('topic22', models.CharField(max_length=20)),
                ('topic23', models.CharField(max_length=20)),
                ('topic24', models.CharField(max_length=20)),
                ('topic25', models.CharField(max_length=20)),
                ('topic26', models.CharField(max_length=20)),
                ('topic27', models.CharField(max_length=20)),
                ('topic28', models.CharField(max_length=20)),
                ('topic29', models.CharField(max_length=20)),
                ('topic30', models.CharField(max_length=20)),
                ('topic31', models.CharField(max_length=20)),
                ('topic32', models.CharField(max_length=20)),
                ('topic33', models.CharField(max_length=20)),
                ('topic34', models.CharField(max_length=20)),
                ('topic35', models.CharField(max_length=20)),
                ('topic36', models.CharField(max_length=20)),
                ('topic37', models.CharField(max_length=20)),
                ('topic38', models.CharField(max_length=20)),
                ('topic39', models.CharField(max_length=20)),
                ('topic40', models.CharField(max_length=20)),
                ('topic41', models.CharField(max_length=20)),
                ('topic42', models.CharField(max_length=20)),
                ('topic43', models.CharField(max_length=20)),
                ('topic44', models.CharField(max_length=20)),
                ('topic45', models.CharField(max_length=20)),
                ('topic46', models.CharField(max_length=20)),
                ('topic47', models.CharField(max_length=20)),
                ('topic48', models.CharField(max_length=20)),
                ('topic49', models.CharField(max_length=20)),
                ('topic50', models.CharField(max_length=20)),
                ('topic51', models.CharField(max_length=20)),
                ('topic52', models.CharField(max_length=20)),
                ('topic53', models.CharField(max_length=20)),
                ('topic54', models.CharField(max_length=20)),
                ('topic55', models.CharField(max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pretestspeaking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vocabulary', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('vowel', models.CharField(max_length=20)),
                ('time', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exercisescratch',
            name='groups',
            field=models.ForeignKey(to='english.group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercisescratch',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='groups',
            field=models.ForeignKey(to='english.group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='database',
            name='vowel',
            field=models.ForeignKey(to='english.phoneme'),
            preserve_default=True,
        ),
    ]
