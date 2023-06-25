# Generated by Django 4.2.1 on 2023-06-24 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=500, null=True, unique=True)),
                ('course_video', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('admin_name', models.CharField(max_length=500, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('phone_number', models.IntegerField(unique=True)),
                ('address', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100, null=True, unique=True)),
                ('class_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.class')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_Private',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, unique=True)),
                ('last_name', models.CharField(max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('phone_number', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('CV', models.FileField(upload_to='')),
                ('identity_card', models.FileField(upload_to='')),
                ('hour_salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=200, null=True, unique=True)),
                ('unit_title', models.CharField(max_length=500, null=True, unique=True)),
                ('subject_num', models.IntegerField()),
                ('subject_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('academic_ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, unique=True)),
                ('last_name', models.CharField(max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('presence_num', models.IntegerField(default=0)),
                ('absence_num', models.IntegerField(default=0)),
                ('done_homework_num', models.IntegerField(default=0)),
                ('late_homework_num', models.IntegerField(default=0)),
                ('evaluation', models.CharField(max_length=50, null=True)),
                ('class_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.class')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_title', models.CharField(max_length=500, null=True, unique=True)),
                ('expalne_photo', models.FileField(upload_to='')),
                ('first_choose', models.CharField(max_length=500, null=True, unique=True)),
                ('second_choose', models.CharField(max_length=500, null=True, unique=True)),
                ('third_choose', models.CharField(max_length=500, null=True, unique=True)),
                ('answer_quiz', models.IntegerField()),
                ('course_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=500, null=True, unique=True)),
                ('date_submit', models.DateField()),
                ('course_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.course')),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True, unique=True)),
                ('last_name', models.CharField(max_length=100, null=True, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('phone_number', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('student_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Expalne_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explane_title', models.CharField(max_length=500, null=True, unique=True)),
                ('expalne_photo', models.FileField(upload_to='')),
                ('expalne_audio', models.FileField(upload_to='')),
                ('text_one', models.CharField(max_length=200, null=True, unique=True)),
                ('course_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='unit_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.unit'),
        ),
        migrations.AddField(
            model_name='class',
            name='school_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school_admin_app.school'),
        ),
    ]