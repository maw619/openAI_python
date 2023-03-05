# Generated by Django 4.1.7 on 2023-03-04 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.TextField()),
                ('answer', models.TextField()),
            ],
            options={
                'db_table': 'chat',
                'managed': True,
            },
        ),
    ]
