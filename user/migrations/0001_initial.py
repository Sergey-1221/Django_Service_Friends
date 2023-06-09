# Generated by Django 4.1.6 on 2023-05-13 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_user_id', models.IntegerField()),
                ('second_user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Friend_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.IntegerField()),
                ('recipient_id', models.IntegerField()),
            ],
        ),
    ]
