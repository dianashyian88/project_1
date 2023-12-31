# Generated by Django 4.2.4 on 2023-09-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='stories/', verbose_name='изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('public_flg', models.BooleanField(blank=True, null=True, verbose_name='признак публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='признак публикации')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
                'ordering': ('id',),
            },
        ),
    ]
