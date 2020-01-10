# Generated by Django 3.0.2 on 2020-01-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200107_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dewey',
            options={'ordering': ['number']},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['reference']},
        ),
        migrations.RemoveField(
            model_name='publication',
            name='type',
        ),
        migrations.AddField(
            model_name='publication',
            name='type_publication',
            field=models.CharField(choices=[('_', 'Indéfini'), ('B', 'Livres'), ('M', 'Musique'), ('F', 'Film')], default='_', max_length=1),
        ),
        migrations.AlterField(
            model_name='dewey',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='publication',
            name='reference',
            field=models.CharField(editable=False, max_length=61),
        ),
    ]