# Generated by Django 3.0.3 on 2020-04-08 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0003_duties_leaves_monthlyinformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaves',
            name='user',
        ),
        migrations.RemoveField(
            model_name='monthlyinformation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Duties',
        ),
        migrations.DeleteModel(
            name='Leaves',
        ),
        migrations.DeleteModel(
            name='MonthlyInformation',
        ),
    ]
