from django.db import models

from workers.models import Worker

class Workgroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Worker, through="Membership")
    subgroups = models.ManyToManyField("self", blank=True,symmetrical=False)
    def __str__(self):
        return self.name

class Membership(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    workgroup = models.ForeignKey(Workgroup, on_delete=models.CASCADE) # TODO: exclude self
    is_supervisor = models.BooleanField(default=False)
    date_joined = models.DateField()

#TODO: add roles to workgroups