# Generated by Django 4.2.3 on 2023-07-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='image',
            field=models.ImageField(default='https://loremflickr.com/cache/resized/65535_52553522454_bb3eef25df_320_320_nofilter.jpg', upload_to='plane_images'),
        ),
    ]
