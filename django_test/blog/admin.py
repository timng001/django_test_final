from django.contrib import admin
from .models import Post

# Register your models here.
#To show posts on admin page
admin.site.register(Post)