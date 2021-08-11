from django.contrib import admin
from user.models import User

from django.contrib.auth.models import Group

admin.site.unregister(Group)

class UserAdmin(admin.ModelAdmin):
    fields=['first_name','last_name', 'email', 'language',]
    readonly_fields = ('updated_at', 'created_at',)
    ordering=('id',)
    

admin.site.register(User)
