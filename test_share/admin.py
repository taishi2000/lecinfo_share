from django.contrib import admin
from .models import Test_Image

class TestImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'subject']

admin.site.register(Test_Image, TestImageAdmin)

