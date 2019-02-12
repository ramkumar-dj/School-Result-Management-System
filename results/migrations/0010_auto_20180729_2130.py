# Generated by Django 2.0.7 on 2018-07-29 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_auto_20180729_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='absent_status',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', help_text='If anyone absent in exam, please added marks=0 check Yes', max_length=1, verbose_name='Absent Check'),
        ),
    ]