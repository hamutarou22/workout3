# Generated by Django 3.2 on 2021-05-22 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0)),
                ('set_number', models.IntegerField(default=0)),
                ('training_date', models.DateTimeField(verbose_name='date published')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workoutapp.event')),
            ],
        ),
    ]
