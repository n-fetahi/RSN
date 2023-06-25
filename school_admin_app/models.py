import email
from django.db import models

# Create your models here.

class School(models.Model):
    name=models.CharField(null=True,unique=True,max_length=200)
    admin_name=models.CharField(null=True,max_length=500)
    password=models.CharField(null=True,max_length=100)
    email=models.EmailField(null=True)
    phone_number=models.IntegerField(unique=True)
    address=models.CharField(null=True,max_length=300)

    def __str__(self) :
        return self.name

class Class(models.Model):
    class_name=models.CharField(null=True,max_length=100)
    school_ID=models.ForeignKey(School,on_delete=models.PROTECT)

    def __str__(self) :
        return self.class_name

class Student(models.Model):
    academic_ID=models.BigAutoField(primary_key=True,auto_created=True,serialize=False, verbose_name='ID')
    first_name=models.CharField(null=True,max_length=100)
    last_name=models.CharField(null=True,max_length=100)
    class_ID=models.ForeignKey(Class,on_delete=models.PROTECT)
    password=models.CharField(null=True,max_length=100)
    presence_num=models.IntegerField(default=0)
    absence_num=models.IntegerField(default=0)
    done_homework_num=models.IntegerField(default=0)
    late_homework_num=models.IntegerField(default=0)
    evaluation=models.CharField(null=True,max_length=50)

    def __str__(self) :
        return self.first_name + self.last_name


class Subject(models.Model):
    subject_name=models.CharField(null=True,max_length=100)
    class_ID=models.ForeignKey(Class,on_delete=models.PROTECT)

    def __str__(self) :
        return self.subject_name


class Unit(models.Model):
    unit_name=models.CharField(null=True,max_length=200)
    unit_title=models.CharField(null=True,max_length=500)
    subject_num=models.IntegerField()
    subject_ID=models.ForeignKey(Subject,on_delete=models.PROTECT)

    def __str__(self) :
        return self.unit_name

class Course(models.Model):
    course_name=models.CharField(null=True,max_length=500)
    course_video=models.FileField()
    unit_ID=models.ForeignKey(Unit,on_delete=models.PROTECT)

    def __str__(self) :
        return self.course_name
    
class Expalne_Course(models.Model):
    explane_title=models.CharField(null=True,max_length=500)
    expalne_photo=models.FileField()
    expalne_audio=models.FileField()
    text_one=models.CharField(null=True,max_length=200)
    text_tow=models.CharField(null=True,max_length=200)
    course_ID=models.ForeignKey(Course,on_delete=models.PROTECT)

    def __str__(self) :
        return self.explane_title
    
class Quiz_Course(models.Model):
    quiz_title=models.CharField(null=True,max_length=500)
    expalne_photo=models.FileField()
    first_choose=models.CharField(null=True,max_length=500)
    second_choose=models.CharField(null=True,max_length=500)
    third_choose=models.CharField(null=True,max_length=500)
    answer_quiz=models.IntegerField()
    course_ID=models.ForeignKey(Course,on_delete=models.PROTECT)

    def __str__(self) :
        return self.quiz_title

class Homework(models.Model):
    course_name=models.CharField(null=True,max_length=500)
    date_submit=models.DateField()
    course_ID=models.ForeignKey(Course,on_delete=models.PROTECT)

    def __str__(self) :
        return self.course_name

class Guardian(models.Model):
    first_name=models.CharField(null=True,max_length=100)
    last_name=models.CharField(null=True,max_length=100)
    password=models.CharField(null=True,max_length=100)
    phone_number=models.IntegerField(unique=True)
    email=models.EmailField(null=True,unique=True)
    student_ID=models.ForeignKey(Student,on_delete=models.PROTECT)

    def __str__(self) :
        return self.first_name + self.last_name


class Teacher_Private(models.Model):
    first_name=models.CharField(null=True,max_length=100)
    last_name=models.CharField(null=True,max_length=100)
    password=models.CharField(null=True,max_length=100)
    phone_number=models.IntegerField(unique=True)
    email=models.EmailField(null=True,unique=True)
    CV=models.FileField()
    identity_card=models.FileField()
    hour_salary=models.IntegerField()

    








    

    

