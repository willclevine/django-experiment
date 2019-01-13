from django.contrib import admin

# Register your models here.
from django.contrib import admin
from api.models import (
    Article,
    Person,
    Similarity,
    Tag,
    Rated,
    PersonAssignment,
    TagAssignment,
    Video,
    View,
)


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


make_published.short_description = "Mark selected stories as published"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person)
admin.site.register(Similarity)
admin.site.register(Tag)
admin.site.register(PersonAssignment)
admin.site.register(TagAssignment)
admin.site.register(Video)
admin.site.register(View)
