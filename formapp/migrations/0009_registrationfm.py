# Generated by Django 3.0.6 on 2020-06-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formapp', '0008_delete_registrationfm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrationfm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('Img1', models.ImageField(upload_to='images/')),
                ('Img2', models.ImageField(upload_to='images/')),
            ],
        ),
    ]