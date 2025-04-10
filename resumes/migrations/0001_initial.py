# Generated by Django 5.1.6 on 2025-02-10 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='resumes/')),
                ('score', models.FloatField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
