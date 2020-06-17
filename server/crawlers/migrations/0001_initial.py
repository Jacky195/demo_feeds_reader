# Generated by Django 2.2 on 2020-06-16 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_code', models.CharField(max_length=100)),
                ('author', models.TextField(default='')),
                ('title', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('original_url', models.TextField(default='')),
                ('date_published', models.DateTimeField(null=True)),
                ('date_fetched', models.DateTimeField(null=True)),
            ],
        ),
    ]
