# Generated by Django 3.2.12 on 2023-03-15 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('body', models.CharField(max_length=255, verbose_name='body')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.category')),
            ],
        ),
    ]