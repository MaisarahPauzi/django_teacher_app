# Generated by Django 2.2.6 on 2019-10-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
