from django.db import models


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     email = models.EmailField(max_length=85, unique=True)
#     password = models.TextField(max_length=200)

#     def __str__(self):
#         return self.email


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    rank = models.PositiveIntegerField()
    name = models.CharField(max_length=30)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_rank = models.PositiveIntegerField(default=0)
    note_rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    rank = models.PositiveIntegerField()
    title = models.CharField(max_length=999)
    content = models.TextField(max_length=19999)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    rank = models.PositiveIntegerField()
    label = models.CharField(max_length=51, unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    notes = models.ManyToManyField(Note)

    def __str__(self):
        return self.label
