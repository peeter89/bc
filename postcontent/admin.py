from django.contrib import admin
from .models import Author,Hashtag, Post
# Register your models here.


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author', 'date_create')
    list_filter = ('author',)

    fieldsets = (
        (None, {
            'fields': ('name', 'author')
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name' , 'last_name', 'slug', 'date_of_birth', 'description', 'date_create')

	fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'description')
        }),
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('name' , 'author', 'slug', 'display_hashtag', 'date_create', 'date_update', 'date_publish', 'is_publish')
	list_filter = ('author', 'slug', 'hashtag', 'date_publish',)

	fieldsets = (
        (None, {
            'fields': ('name', 'author', 'hashtag', 'date_publish')
        }),
    )
