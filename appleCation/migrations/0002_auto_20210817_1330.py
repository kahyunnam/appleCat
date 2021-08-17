# Generated by Django 3.1.4 on 2021-08-17 17:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appleCation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apple',
            name='OAdue',
        ),
        migrations.RemoveField(
            model_name='apple',
            name='OAlink',
        ),
        migrations.RemoveField(
            model_name='apple',
            name='OAstatus',
        ),
        migrations.RemoveField(
            model_name='apple',
            name='OAthoughts',
        ),
        migrations.RemoveField(
            model_name='apple',
            name='interviewDate',
        ),
        migrations.RemoveField(
            model_name='apple',
            name='interviewInvite',
        ),
        migrations.RemoveField(
            model_name='apple',
            name='statusCheck',
        ),
        migrations.AlterField(
            model_name='apple',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='accessKey',
            field=models.CharField(default='NEWCAT', max_length=200),
        ),
        migrations.AlterField(
            model_name='cat',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='AppleOA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OAName', models.CharField(default=' ', max_length=20)),
                ('OADue', models.DateTimeField(blank=True, null=True)),
                ('OALink', models.TextField(blank=True, null=True)),
                ('OAStatus', models.CharField(default='Not Completed', max_length=20)),
                ('OARef', models.CharField(default='None', max_length=5)),
                ('apple', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appleCation.apple')),
            ],
        ),
        migrations.CreateModel(
            name='AppleInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviewName', models.CharField(default=' ', max_length=50)),
                ('interviewDate', models.DateTimeField(default=datetime.date.today)),
                ('interviewLink', models.TextField(blank=True, null=True)),
                ('interviewStatus', models.CharField(default='Not Completed', max_length=20)),
                ('interviewRef', models.CharField(default='None', max_length=5)),
                ('apple', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appleCation.apple')),
            ],
        ),
    ]