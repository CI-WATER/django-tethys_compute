from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone


class Cluster(models.Model):
    name = models.CharField(max_length=30)
    size = models.IntegerField()

class TethysJob(models.Model):
    STATUSES = (
        ('PEN', 'Pending'),
        ('SUB', 'Submitted'),
        ('RUN', 'Running'),
        ('COM', 'Complete'),
        ('ERR', 'Error'),
    )
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)
    group = models.CharField(max_length=30)
    creation_time = models.DateTimeField(default=timezone.now())
    submission_time = models.DateTimeField()
    completion_time = models.DateTimeField()
    status = models.CharField(max_length=3, choices=STATUSES)

    def execute(self):
        """

        :return:
        """
        pass

    def stop(self):
        """

        :return:
        """
        pass

    def pause(self):
        """

        :return:
        """
        pass

class CondorJob(TethysJob):
    scheduler = models.CharField(max_length=12)
    ami = models.CharField(max_length=9)

    @property
    def condorpy_job(self):
        pass