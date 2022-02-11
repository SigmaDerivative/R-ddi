from django.contrib import admin
from .models import Estate, Belongings, Status, Comment

# Register your models here.
@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Belongings)
class BelongingsAdmin(admin.ModelAdmin):
    list_display = ('estate', 'name', 'description')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('belonging', 'user', 'alternatives', 'rating')

@admin.register(Comment)
class CommentsAmin(admin.ModelAdmin):
    list_display = ('user', 'belonging', 'body')
