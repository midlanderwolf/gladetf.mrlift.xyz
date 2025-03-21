# Generated by Django 5.1.5 on 2025-01-20 16:35

import vehicles.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0010_remove_historicallivery_css_remove_livery_css_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallivery',
            name='show_name',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='livery',
            name='show_name',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='historicallivery',
            name='colour',
            field=vehicles.fields.ColourField(help_text='For the most simplified version of the livery', max_length=7),
        ),
        migrations.AlterField(
            model_name='historicallivery',
            name='colours',
            field=vehicles.fields.ColoursField(blank=True, help_text='Left and right CSS will be generated from this', max_length=512),
        ),
        migrations.AlterField(
            model_name='historicallivery',
            name='left_css',
            field=vehicles.fields.CSSField(blank=True, help_text='Automatically generated from colours and angle', max_length=1024, verbose_name='Left CSS'),
        ),
        migrations.AlterField(
            model_name='historicallivery',
            name='published',
            field=models.BooleanField(default=False, help_text='Tick to include in the CSS and be able to apply this livery to vehicles'),
        ),
        migrations.AlterField(
            model_name='historicallivery',
            name='right_css',
            field=vehicles.fields.CSSField(blank=True, help_text='Should be a mirror image of the left CSS', max_length=1024, verbose_name='Right CSS'),
        ),
        migrations.AlterField(
            model_name='historicallivery',
            name='stroke_colour',
            field=vehicles.fields.ColourField(blank=True, help_text='Use sparingly, often looks shit', max_length=7),
        ),
        migrations.AlterField(
            model_name='historicallivery',
            name='text_colour',
            field=vehicles.fields.ColourField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='livery',
            name='colour',
            field=vehicles.fields.ColourField(help_text='For the most simplified version of the livery', max_length=7),
        ),
        migrations.AlterField(
            model_name='livery',
            name='colours',
            field=vehicles.fields.ColoursField(blank=True, help_text='Left and right CSS will be generated from this', max_length=512),
        ),
        migrations.AlterField(
            model_name='livery',
            name='left_css',
            field=vehicles.fields.CSSField(blank=True, help_text='Automatically generated from colours and angle', max_length=1024, verbose_name='Left CSS'),
        ),
        migrations.AlterField(
            model_name='livery',
            name='published',
            field=models.BooleanField(default=False, help_text='Tick to include in the CSS and be able to apply this livery to vehicles'),
        ),
        migrations.AlterField(
            model_name='livery',
            name='right_css',
            field=vehicles.fields.CSSField(blank=True, help_text='Should be a mirror image of the left CSS', max_length=1024, verbose_name='Right CSS'),
        ),
        migrations.AlterField(
            model_name='livery',
            name='stroke_colour',
            field=vehicles.fields.ColourField(blank=True, help_text='Use sparingly, often looks shit', max_length=7),
        ),
        migrations.AlterField(
            model_name='livery',
            name='text_colour',
            field=vehicles.fields.ColourField(blank=True, max_length=7),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='colours',
            field=vehicles.fields.ColoursField(blank=True, max_length=255),
        ),
    ]
