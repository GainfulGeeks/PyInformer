from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from workers.models import WorkLog, Worker


class WorkerInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = "workers"


class UserAdmin(BaseUserAdmin):
    inlines = [WorkerInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Worker)


class WorkLogAdmin(admin.ModelAdmin):
    list_display = ("log_date", "worker", "duration")


admin.site.register(WorkLog, WorkLogAdmin)
