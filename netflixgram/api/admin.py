from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User, Group
from .models import Profile, Review

admin.site.unregister(User)

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(Review)

