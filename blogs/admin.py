from django.contrib import admin
from blogs.models import Blog, Comment, Category


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3
    fieldsets = [

        ('Advanced', {'fields': ('user', 'comment'), 'classes': ['collapse']}),

    ]


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['pub_date']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['category']}),
        (None, {'fields': ['page_slug']}),
        ('Advanced', {'fields': ['is_comment']}),
    ]
    inlines = [CommentInline]


admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['page_slug']}),
    ]


admin.site.register(Category, CategoryAdmin)