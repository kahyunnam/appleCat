# Generated by Django 3.1.4 on 2021-08-17 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appleCation', '0002_auto_20210817_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apple',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appleCation.cat', to_field='accessKey'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='accessKey',
            field=models.CharField(default='NEWCAT', max_length=200, unique=True),
        ),
    ]
