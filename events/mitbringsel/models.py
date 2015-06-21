from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class TemporalMixin(models.Model):
    created_by = models.ForeignKey(User, editable=False, related_name='%(class)s_created_by')
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_by = models.ForeignKey(User, editable=False, related_name='%(class)s_modified_by')
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CommentableMixin(models.Model):
    comment = models.CharField(blank=True, max_length=600)

    class Meta:
        abstract = True

class MitbringselType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Mitbringsel(CommentableMixin, TemporalMixin):
    text = models.CharField(max_length=200)
    type = models.ForeignKey(MitbringselType)
    definitiv = models.BooleanField(default=False)

    def __str__(self):
        return self.text


