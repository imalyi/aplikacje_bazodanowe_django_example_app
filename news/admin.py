from django.contrib import admin
from news.models import News, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','icon')
    prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(News)
admin.site.register(Category)

