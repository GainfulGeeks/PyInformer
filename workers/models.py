from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Worker(models.Model):
    class WorkerTypeChoices(models.TextChoices):
        EMPLOYEE = "EMP", _("Employee")
        FREELANCER = "FRL", _("Freelancer")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=4, choices=WorkerTypeChoices, default=WorkerTypeChoices.EMPLOYEE
    )
    ssn = models.CharField(
        max_length=10, null=True, blank=True, verbose_name=_("Social Security Number")
    )

    def __str__(self):
        return (
            f"{self.user.first_name} {self.user.last_name} ({self.get_type_display()})"
        )
    # TODO: add primary role


class WorkLog(models.Model):
    log_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    remarks = models.TextField()
    worker = models.ForeignKey(
        Worker, related_name="reported_work_logs", on_delete=models.CASCADE
    )
    reviewer = models.ForeignKey(
        Worker, related_name="assigned_work_logs", null=True, on_delete=models.SET_NULL
    )
    #TODO: probably separate the model for work log review
    #TODO: probably move worklog to another app
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Work done by {self.worker} on {self.log_date}"

    @property
    def duration(self):
        date = self.log_date
        start_datetime = datetime.combine(date, self.start_time)
        end_datetime = datetime.combine(date, self.end_time)
        duration = end_datetime - start_datetime
        seconds = duration.total_seconds()
        hours = int(seconds // 3600)
        minutes = int(((seconds % 3600) // 60))

        return f"{hours} hr(s) and {minutes} min(s)"
