from django.contrib import admin


from workers.models import Worker
from workgroups.models import Workgroup


class MembershipInline(admin.TabularInline):
    model = Workgroup.members.through
    can_delete = False
    verbose_name_plural = "members"

# class SubgroupInline(admin.StackedInline):
#     model = Workgroup.subgroups.through
#     can_delete = False
#     verbose_name_plural = "subgroups"

class WorkgroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [MembershipInline]
    exclude = ["members"]

admin.site.register(Workgroup, WorkgroupAdmin)

