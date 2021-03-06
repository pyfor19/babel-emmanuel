# Generated by Django 3.0.2 on 2020-01-07 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200107_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dewey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=61)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=61)),
                ('reference', models.CharField(max_length=61)),
                ('type', models.CharField(max_length=5)),
                ('genre', models.CharField(max_length=35)),
                ('date_publication', models.DateField(blank=True, null=True)),
                ('label_editor', models.CharField(blank=True, max_length=50, null=True)),
                ('nb_tracks_pages', models.IntegerField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.Author')),
                ('dewey_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.Dewey')),
            ],
        ),
    ]
