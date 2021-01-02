# Generated by Django 3.1.4 on 2021-01-07 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0002_auto_20210107_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_photo', models.URLField(default='https://ac101-image.s3.us-east-2.amazonaws.com/add-photo-portrait.png', max_length=2000, null=True)),
                ('thumbnail', models.URLField(default='https://ac101-image.s3.us-east-2.amazonaws.com/add-photo-portrait.png', max_length=2000, null=True)),
                ('summary_photo', models.URLField(default='https://ac101-image.s3.us-east-2.amazonaws.com/add-photo-portrait.png', max_length=2000, null=True)),
                ('specific_category', models.CharField(max_length=150, null=True)),
                ('expiry_date', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.course')),
            ],
            options={
                'db_table': 'course_requests',
            },
        ),
        migrations.CreateModel(
            name='RequestFormStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'request_form_status',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.courserequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'supports',
            },
        ),
        migrations.CreateModel(
            name='RequestCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.courserequest')),
                ('voter', models.ManyToManyField(related_name='request_votes', to='user.User')),
            ],
            options={
                'db_table': 'request_curriculums',
            },
        ),
        migrations.CreateModel(
            name='RequestCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField(default='https://ac101-image.s3.us-east-2.amazonaws.com/add-photo-portrait.png', max_length=2000, null=True)),
                ('description', models.CharField(max_length=150)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.courserequest')),
            ],
            options={
                'db_table': 'request_cards',
            },
        ),
        migrations.AddField(
            model_name='courserequest',
            name='form_status',
            field=models.ManyToManyField(to='request.RequestFormStatus'),
        ),
        migrations.AddField(
            model_name='courserequest',
            name='liker',
            field=models.ManyToManyField(related_name='liked_requests', to='user.User'),
        ),
        migrations.AddField(
            model_name='courserequest',
            name='tag',
            field=models.ManyToManyField(to='request.Tag'),
        ),
    ]
