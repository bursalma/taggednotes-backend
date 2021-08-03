# Generated by Django 3.2.5 on 2021-08-03 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggednotes', '0008_alter_tag_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='rank',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='note',
            name='section',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='taggednotes.section'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='section',
            name='note_rank',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='section',
            name='rank',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='section',
            name='tag_rank',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='tag',
            name='label',
            field=models.CharField(blank=True, max_length=51),
        ),
        migrations.AlterField(
            model_name='tag',
            name='notes',
            field=models.ManyToManyField(blank=True, to='taggednotes.Note'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='rank',
            field=models.PositiveIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='tag',
            name='section',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='taggednotes.section'),
        ),
    ]
