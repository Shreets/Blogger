from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created'),


admin.site.register(Blog,BlogAdmin)

# admin.site.register(Author)
