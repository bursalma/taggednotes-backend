from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rank = models.PositiveIntegerField(default=1, blank=True)
    name = models.CharField(max_length=30, blank=True)
    tag_rank = models.PositiveIntegerField(default=1, blank=True)
    note_rank = models.PositiveIntegerField(default=1, blank=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rank = models.PositiveIntegerField(default=1, blank=True)
    title = models.CharField(max_length=999, default='', blank=True)
    content = models.TextField(max_length=19999, default='', blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rank = models.PositiveIntegerField(default=1, blank=True)
    label = models.CharField(max_length=51, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True)
    notes = models.ManyToManyField(Note, blank=True)

    def __str__(self):
        return self.label
