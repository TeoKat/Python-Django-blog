# Generated by Django 3.0.4 on 2020-03-23 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20200323_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='article.Article'),
        ),
    ]