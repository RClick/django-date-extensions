from django.db import models

from django_date_extensions.fields import ApproximateDateField


class ApproximateTimeDelta(models.Model):
    date_from = ApproximateDateField()
    date_to = ApproximateDateField()
