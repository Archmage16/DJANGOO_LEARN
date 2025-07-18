# Generated by Django 5.2.3 on 2025-06-30 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('position', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('course_name', models.TextField()),
                ('start_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('employee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='school.employee')),
                ('subject', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('school.employee',),
        ),
        migrations.CreateModel(
            name='OrderedStudent',
            fields=[
            ],
            options={
                'verbose_name': 'Ordered_Students',
                'ordering': ['-created_time'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('school.student',),
        ),
    ]
