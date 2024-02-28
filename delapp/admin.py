from django.contrib import admin
from .models import Student
from .models import  Staff
from .models import  Department
from  .models import  Post

# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Post)

