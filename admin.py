from django.contrib import admin
from .models import Publisher, Author, Book


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'createdBy', 'status')
    list_filter = ('city', 'country', 'createdBy')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'posted'
    ordering = ['status', 'posted']


admin.site.register(Publisher, PublisherAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'createdBy', 'status')
    list_filter = ('createdBy', 'posted','BookAuthors')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('salutation', 'name',)}
    date_hierarchy = 'posted'
    ordering = ['status', 'posted']


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'posted', 'status')
    list_filter = ('genre', 'status', 'posted', 'authors')
    search_fields = ('title', 'genre')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'posted'
    ordering = ['status', 'posted']


admin.site.register(Book, BookAdmin)
