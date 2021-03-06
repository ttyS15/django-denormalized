# Generated by Django 2.1.3 on 2018-12-03 06:28

import denormalized.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='points_sum',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='group',
            field=denormalized.models.DenormalizedForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Group'),
        ),
    ]
