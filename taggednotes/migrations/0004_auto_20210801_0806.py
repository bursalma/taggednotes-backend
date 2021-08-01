# Generated by Django 3.2.5 on 2021-08-01 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggednotes', '0003_alter_section_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='section',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='section',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tag',
            name='rank',
            field=models.PositiveIntegerField(default=0),
        ),
    ]