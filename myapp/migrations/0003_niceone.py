# Generated by Django 4.0.3 on 2022-05-17 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_link_old_price_alter_link_price_difference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niceone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('url', models.URLField()),
                ('current_price', models.FloatField(blank=True)),
                ('old_price', models.FloatField(default=0)),
                ('price_difference', models.FloatField(default=0)),
                ('updated', models.DateField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['price_difference', '-created'],
            },
        ),
    ]
