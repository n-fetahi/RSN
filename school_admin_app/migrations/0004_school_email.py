# Generated by Django 4.2.1 on 2023-06-25 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin_app', '0003_expalne_course_text_tow'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
