# Generated by Django 3.2.3 on 2021-05-24 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('npo_user', '0001_initial'),
        ('npo_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='npo_news.news')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='npo_user.npouser')),
            ],
        ),
    ]