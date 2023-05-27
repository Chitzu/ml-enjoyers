from django.contrib import admin
from .models import *
# Register your models here.


class ContextInline(admin.TabularInline):
    model = Context
    extra = 1


class AdAdmin(admin.ModelAdmin):
    inlines = [ContextInline]


class HistoryInline(admin.TabularInline):
    model = History
    extra = 1
    

class SessionAdmin(admin.ModelAdmin):
    inlines = [HistoryInline]


admin.site.register(Session, SessionAdmin)
admin.site.register(Ad, AdAdmin)
