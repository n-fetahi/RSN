from django.contrib import admin
from school_admin_app import models

# Register your models here.
admin.site.register(models.School)
admin.site.register(models.Class)
admin.site.register(models.Student)
admin.site.register(models.Subject  )
admin.site.register(models.Unit)
admin.site.register(models.Course)
admin.site.register(models.Expalne_Course)
admin.site.register(models.Quiz_Course)
admin.site.register(models.Guardian)
