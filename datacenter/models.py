import datetime

from django.utils import timezone
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        leaved_time = timezone.localtime()
        if self.leaved_at is not None:
            leaved_time = timezone.localtime(self.leaved_at)
        return int(
            (leaved_time - timezone.localtime(self.entered_at))
            .total_seconds())

    def format_duration(self):
        duration = self.get_duration()
        return "{:02d}:{:02d}:{:02d}".format(
            duration // 3600, duration % 3600 // 60, duration % 60
            )

    def is_visit_long(self, minutes=60):
        return self.get_duration() // 60 >= minutes
