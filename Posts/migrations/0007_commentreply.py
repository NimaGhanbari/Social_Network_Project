# Generated by Django 3.2 on 2023-03-31 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts', '0006_remove_comment_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1048)),
                ('is_approved', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('parentComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CommentReply',
                'verbose_name_plural': 'CommentReplys',
                'db_table': 'CommentReplys',
            },
        ),
    ]