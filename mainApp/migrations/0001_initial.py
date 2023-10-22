# Generated by Django 4.2.6 on 2023-10-22 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('date_of_birth', models.DateField(verbose_name='Date of birth: ')),
                ('number_of_book', models.PositiveSmallIntegerField()),
                ('alive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('page', models.PositiveSmallIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.author')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('working_time', models.CharField(choices=[('06:00 dan 12:00 gacha', '06:00 dan 12:00 gacha'), ('12:00 dan 18:00 gacha', '12:00 dan 18:00 gacha'), ('18:00 dan 23:59 gacha', '18:00 dan 23:59 gacha')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course', models.PositiveSmallIntegerField()),
                ('number_of_book', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_recieved', models.DateField()),
                ('isreturned', models.BooleanField(default=False)),
                ('date_of_returned', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.book')),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.librarian')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.student')),
            ],
        ),
    ]