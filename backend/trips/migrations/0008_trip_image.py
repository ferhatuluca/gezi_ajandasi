# Generated by Django 3.0.4 on 2020-04-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20200328_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
