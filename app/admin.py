from django.contrib import admin
from .models import Comment, Subject, Like

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'professor']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'user']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)

