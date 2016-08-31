from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import *

#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('paycheck',)}),
    )


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )


class MemberAdmin(admin.ModelAdmin):
    list_display = ('team', 'user', )


class WorkAdmin(admin.ModelAdmin):
    list_display = ('date', 'member', 'period')


class PeriodAdmin(admin.ModelAdmin):
    list_display = ('team', 'unit',)



admin.site.register(User, MyUserAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Period, PeriodAdmin)
