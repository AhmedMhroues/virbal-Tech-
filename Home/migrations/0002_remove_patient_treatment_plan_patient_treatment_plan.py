# Generated by Django 5.0.6 on 2024-06-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='treatment_plan',
        ),
        migrations.AddField(
            model_name='patient',
            name='treatment_plan',
            field=models.ManyToManyField(blank=True, default='طماطم', null=True, related_name='patients', to='Home.training'),
        ),
    ]
