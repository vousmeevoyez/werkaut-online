# Generated by Django 4.1.9 on 2023-07-27 07:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('nutrition', '0015_alter_ingredient_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logitem',
            options={'ordering': ['-datetime']},
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='creation_date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='update_date',
            new_name='last_update',
        ),
    ]
