# Generated by Django 2.2.7 on 2021-03-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voting_process', '0008_candidate_candidate_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='vote_position',
            field=models.CharField(default='president', max_length=100),
            preserve_default=False,
        ),
    ]
