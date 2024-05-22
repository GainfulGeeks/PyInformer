from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Worker(models.Model):
    class WorkerTypeChoices(models.TextChoices):
        EMPLOYEE = "EMP", _("Employee")
        FREELANCER = "FRL", _("Freelancer")
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=WorkerTypeChoices,default=WorkerTypeChoices.EMPLOYEE)
    ssn = models.CharField(max_length=10,null=True,blank=True,verbose_name=_("Social Security Number"))
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.get_type_display()})"

