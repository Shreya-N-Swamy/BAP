# Generated by Django 2.1.4 on 2019-01-05 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=30, unique_for_date='posted')),
                ('email', models.EmailField(max_length=254)),
                ('headshot', models.ImageField(upload_to='author_headshots')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('posted', 'Posted')], default='draft', max_length=10)),
                ('posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BAP_Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=30, unique_for_date='posted')),
                ('genere', models.CharField(choices=[('fiction', 'Fiction'), ('pureScience', 'PureScience'), ('education', 'Education'), ('childrens', 'Childrens')], default='fiction', max_length=15)),
                ('publication_date', models.DateField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('posted', 'Posted')], default='draft', max_length=10)),
                ('posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(to='BAP.Author')),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BAP_Book', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-genere'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30, unique_for_date='posted')),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('posted', 'Posted')], default='draft', max_length=10)),
                ('posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BAP_Publisher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BAP.Publisher'),
        ),
    ]