# Generated by Django 3.0.4 on 2020-03-20 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20200319_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default='???', max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(),
        ),
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
