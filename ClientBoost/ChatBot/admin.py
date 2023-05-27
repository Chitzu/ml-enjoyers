from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Ad)


class HistoryInline(admin.TabularInline):
    model = History
    extra = 1
    

class SessionAdmin(admin.ModelAdmin):
    inlines = [HistoryInline]


admin.site.register(Session, SessionAdmin)