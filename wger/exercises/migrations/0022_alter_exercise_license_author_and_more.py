# Generated by Django 4.1.5 on 2023-02-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0021_deletionlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
        migrations.AlterField(
            model_name='exercisebase',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
        migrations.AlterField(
            model_name='exerciseimage',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
        migrations.AlterField(
            model_name='exercisevideo',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
        migrations.AlterField(
            model_name='historicalexercise',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
        migrations.AlterField(
            model_name='historicalexercisebase',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
        migrations.AlterField(
            model_name='historicalexerciseimage',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
        migrations.AlterField(
            model_name='historicalexercisevideo',
            name='license_author',
            field=models.CharField(
                blank=True,
                help_text=
                'If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.',
                max_length=60,
                null=True,
                verbose_name='Author'
            ),
        ),
    ]
