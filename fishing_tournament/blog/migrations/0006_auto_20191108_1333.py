# Generated by Django 2.1.5 on 2019-11-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_pics/default.jpg', upload_to='post_pics/', verbose_name='Bild'),
        ),
    ]
