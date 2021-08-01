from django.db import models
from django.contrib.auth.models import User


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rank = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=30)
    tag_rank = models.PositiveIntegerField(default=0)
    note_rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rank = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=999)
    content = models.TextField(max_length=19999)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rank = models.PositiveIntegerField(default=0)
    label = models.CharField(max_length=51, unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    notes = models.ManyToManyField(Note)

    def __str__(self):
        return self.label
