# Generated by Django 2.0.1 on 2018-02-07 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speaker_recognition', '0008_auto_20180207_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identificationProfileId', models.CharField(max_length=200)),
                ('pathNN', models.CharField(max_length=1000, null=True)),
                ('status', models.BooleanField(default=1)),
                ('idCostumer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='speaker_recognition.Customer')),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]