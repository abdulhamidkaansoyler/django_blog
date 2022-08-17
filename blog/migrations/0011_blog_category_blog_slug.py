# Generated by Django 4.1 on 2022-08-14 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]