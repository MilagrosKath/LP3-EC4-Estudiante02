# Generated by Django 4.1.3 on 2022-12-28 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EC4', '0002_alter_course_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='idcourse',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
