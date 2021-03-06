# Generated by Django 3.1 on 2020-09-01 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0002_auto_20200901_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField(default=0)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing')),
            ],
        ),
    ]
