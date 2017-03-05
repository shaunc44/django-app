from django.contrib import admin
#import Post class from the models.py file
from .models import Post


#make model visible on the Admin page
admin.site.register(Post)
