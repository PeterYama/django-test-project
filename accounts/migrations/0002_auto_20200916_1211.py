# Generated by Django 3.1.1 on 2020-09-16 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='VIEW_GROUP_CHOICE',
            field=models.CharField(blank=True, choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'FRIENDS ONLY'), ('PRIVATE', 'PRIVATE')], default='None', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='VIEW_GROUP_CHOICE',
            field=models.CharField(blank=True, choices=[('PUBLIC', 'PUBLIC'), ('PRIVATE', 'FRIENDS ONLY'), ('PRIVATE', 'PRIVATE')], default='None', max_length=500, null=True),
        ),
    ]
