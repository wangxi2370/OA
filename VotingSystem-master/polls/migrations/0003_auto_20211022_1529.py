# Generated by Django 3.2.5 on 2021-10-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_is_checkbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='feedforward',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='is_checkbox',
            field=models.IntegerField(default=0),
        ),
    ]
