# Generated by Django 2.1.3 on 2018-12-16 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='jobportal.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=80)),
                ('logo', models.ImageField(blank=True, upload_to='images/companies')),
                ('website', models.URLField(blank=True, max_length=255)),
                ('info', models.TextField(blank=True)),
                ('category', models.ManyToManyField(blank=True, related_name='companies', to='jobportal.Category')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job_url', models.URLField(blank=True, max_length=255)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=None, related_name='jobs', to='jobportal.Category')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=None, related_name='jobs', to='jobportal.Company')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='jobportal.Location')),
            ],
            options={
                'verbose_name_plural': 'Locations',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='jobs', to='jobportal.Location'),
        ),
        migrations.AddField(
            model_name='job',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ManyToManyField(blank=True, related_name='companies', to='jobportal.Location'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
    ]