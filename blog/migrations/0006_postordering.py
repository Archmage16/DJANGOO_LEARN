# Generated by Django 5.2.3 on 2025-06-30 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_privete2'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostOrdering',
            fields=[
            ],
            options={
                'verbose_name': 'Ordered Post',
                'ordering': ['-created_time'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('blog.post',),
        ),
    ]
