from django.contrib import admin
from .models import Post

# ADD ROWS TO ADMIN POST
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'date_created', 'author')


# Register your models here.
admin.site.register(Post, PostAdmin)
