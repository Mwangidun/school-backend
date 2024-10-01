from django.contrib import admin

# Register your models here.
from .models import Staff,Member,Administrator,CustomUser


admin.site.register(Staff)
admin.site.register(Member)
admin.site.register(Administrator)
admin.site.register(CustomUser)
