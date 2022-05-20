# Generated by Django 4.0.4 on 2022-04-29 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.IntegerField(unique=True)),
                ('score_approve', models.FloatField(blank=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, unique=True)),
                ('tipo', models.IntegerField()),
                ('score', models.FloatField(blank=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.test')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255, unique=True)),
                ('correct', models.BooleanField(blank=True, default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.question')),
            ],
        ),
    ]