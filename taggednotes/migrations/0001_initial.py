# Generated by Django 3.2.5 on 2021-07-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=999)),
                ('content', models.TextField(max_length=19999)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('tag_rank', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.PositiveIntegerField()),
                ('label', models.CharField(max_length=51, unique=True)),
                ('notes', models.ManyToManyField(to='taggednotes.Note')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taggednotes.section')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taggednotes.section'),
        ),
    ]
