
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=653975)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('image_url', models.CharField(max_length=500)),
                ('content', models.CharField(max_length=5000)),
                ('approved', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_posts', to='rareapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='rareapi.post')),
            ],
        ),
        migrations.CreateModel(
            name='RareUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=55)),
                ('profile_image_url', models.CharField(max_length=14000)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('active', models.BigIntegerField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
                ('image_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
                ('posts', models.ManyToManyField(through='rareapi.PostTag', to='rareapi.post')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('ended_on', models.DateField(blank=True, default=None, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='followed_by', to='rareapi.rareuser')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subscription_follower', to='rareapi.rareuser')),
            ],
        ),
        migrations.AddField(
            model_name='posttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='rareapi.tag'),
        ),
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_reactions', to='rareapi.post')),
                ('reaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='rareapi.reaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_react_user', to='rareapi.rareuser')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='reactions',
            field=models.ManyToManyField(related_name='posts_with_reaction', through='rareapi.PostReaction', to='rareapi.reaction'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts_with_tag', through='rareapi.PostTag', to='rareapi.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='rare_user_posts', to='rareapi.rareuser'),
        ),
        migrations.CreateModel(
            name='DemotionQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to='rareapi.rareuser')),
                ('approver_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approver_user', to='rareapi.rareuser')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400000001)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rare_User_Comments', to='rareapi.rareuser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_posts', to='rareapi.post')),
            ],
        ),
    ]
