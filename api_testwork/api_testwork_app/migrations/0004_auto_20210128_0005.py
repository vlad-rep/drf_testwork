# Generated by Django 2.2 on 2021-01-27 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_testwork_app', '0003_remove_answer_answer_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='pub_date',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='poll',
            old_name='upd_date',
            new_name='start_date',
        ),
    ]
