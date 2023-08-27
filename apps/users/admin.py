from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import User
from apps.profiles.models import Profile
from apps.posts.models import Post

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Post)

# Register your models here.
