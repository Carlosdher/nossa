# Generated by Django 2.0.7 on 2018-09-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reposicao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacao',
            name='status',
            field=models.IntegerField(choices=[(0, 'Negada'), (1, 'Andamento'), (2, 'Andamento'), (3, 'Andamento'), (4, 'Aceita')]),
        ),
    ]
