from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content',)
    list_filter = ('date_of_creation', )