# Generated by Django 4.1.7 on 2023-06-15 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0003_rename_author_event_user"),
    ]

    operations = [
        migrations.RenameField(model_name="event", old_name="user", new_name="author",),
    ]