# Generated by Django 3.2.3 on 2021-06-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoAboutJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_journal', models.TextField(blank=True, verbose_name='Чем занимается наше издание')),
                ('address', models.TextField(blank=True, verbose_name='Юридический адрес издания')),
                ('number_one', models.CharField(max_length=20, verbose_name='А1')),
                ('number_two', models.CharField(max_length=20, verbose_name='МТС')),
                ('number_three', models.CharField(max_length=20, verbose_name='Life')),
                ('number_four', models.CharField(max_length=20, verbose_name='Городской телефон')),
                ('location_map', models.ImageField(upload_to='photos_location_map/%Y/%m/%d', verbose_name='Схема проезда')),
            ],
        ),
    ]
