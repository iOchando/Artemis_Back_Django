# Generated by Django 4.0.4 on 2022-07-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_answer_respuesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firma',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
