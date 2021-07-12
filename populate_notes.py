import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

import django
django.setup()

import random
from taggednotes.models import Note, Tag, Section
from faker import Faker
fakegen = Faker()


def populate_sections(n: int):
    for i in range(n):
        section = Section.objects.create(name=fakegen.word(), rank=i,
                                         tag_rank=0, note_rank=0)
        section.save()


def populate_tags(n: int):
    sections = Section.objects.all()

    for _ in range(n):
        section = random.choice(sections)
        section.tag_rank += 1
        tag = Tag.objects.create(rank=section.tag_rank,
                                 label=fakegen.word(),
                                 section=section)
        section.save()
        tag.save()


def populate_notes(n: int, rel: int):
    sections = Section.objects.all()
    tags = Tag.objects.all()

    for _ in range(n):
        section = random.choice(sections)
        section.note_rank += 1
        note = Note.objects.create(rank=section.note_rank,
                                   title=fakegen.sentence(),
                                   content=fakegen.paragraph(),
                                   section=section)
        section.save()
        note.save()
        fil_tags = list(filter(lambda x: x.section == note.section, tags))
        random.shuffle(fil_tags)
        ran = random.randrange(1, rel+1)
        ran = ran if len(fil_tags) > ran else len(fil_tags)

        for tag in fil_tags[:ran]:
            tag.notes.add(note)


if __name__ == '__main__':
    print('populating script')
    populate_sections(2)
    populate_tags(10)
    populate_notes(30, 4)
    print('done')
