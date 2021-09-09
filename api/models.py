from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import year_validation

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['slug']

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Slug жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['slug']

    def __str__(self):
        return self.slug


class Title(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название',
                            null=False)
    year = models.PositiveSmallIntegerField(blank=True, null=True,
                                            verbose_name='Год выпуска',
                                            validators=[year_validation])
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='categories', blank=True,
                                 null=True, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name', 'year']

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(verbose_name='Текст')
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='Произведение')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews', verbose_name='Автор')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True,
                                    null=True)

    class Meta:
        unique_together = ('author', 'title')
        ordering = ['pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name='comments', null=True,
                               verbose_name='Отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
