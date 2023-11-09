from django.db import models
from config.settings import AUTH_USER_MODEL


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    # created_at = models.CharField(max_length=15, verbose_name='наименование', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('id',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', **NULLABLE)
    price = models.FloatField(verbose_name='цена')
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='дата создания')
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='дата обновления', **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='владелец продукта', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('id',)
        permissions = [
            (
                'set_is_published',
                'Can change_is_published продукт'
            ),
            (
                'set_description',
                'Can change_description продукт'
            ),
            (
                'set_category',
                'Can change_category продукт'
            )
        ]


class Story(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое', **NULLABLE)
    image = models.ImageField(upload_to='stories/', verbose_name='изображение', **NULLABLE)
    create_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='дата создания')
    public_flg = models.BooleanField(verbose_name='признак публикации', default=False)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('id',)
