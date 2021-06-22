from django.db import models

from django.urls import reverse


class RubricPublications(models.Model):
    name = models.CharField(max_length=90, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubric', kwargs={'rubric_slug': self.slug})

    class Meta:
        verbose_name = 'Рубрику'
        verbose_name_plural = 'Рубрики'
        ordering = ['id']


class Author(models.Model):

    first_name = models.CharField(max_length=100, verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия автора')
    position = models.CharField(max_length=255, verbose_name='Должность')
    summary = models.TextField(blank=True, verbose_name='Сведения об авторе')
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos_author/%Y/%m/%d", verbose_name='Фото автора')

    def __str__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        return reverse('article_about_author', kwargs={'author_id': self.pk})


class Publications(models.Model):

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    annotations = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Текст статьи')
    photo = models.ImageField(upload_to="photos_publications/%Y/%m/%d", verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    publiched_at = models.BooleanField(default=True)
    category = models.ForeignKey(RubricPublications, on_delete=models.PROTECT, verbose_name='Категория')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Материалы публикаций'
        verbose_name_plural = 'Материалы публикаций'
        ordering = ['time_create', 'title']


class TypesOfSports(models.Model):

    name = models.CharField(max_length=255, verbose_name='Вид спорта')

    def __str__(self):
        return self.name


class Athlete(models.Model):

    first_name = models.CharField(max_length=100, verbose_name='Имя спортсмена')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия спортсмена')
    summary = models.TextField(blank=True, verbose_name='Информация о спортсмене')
    awards = models.TextField(blank=True, verbose_name='Список наград спортсмена')
    photo = models.ImageField(upload_to="photos_athlete/%Y/%m/%d", verbose_name='Фото спортсмена')
    type_sports = models.ForeignKey(TypesOfSports, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('article_about_athlete', kwargs={'athlete_id': self.pk})


class InfoAboutJournal(models.Model):
    about_journal = models.TextField(blank=True, verbose_name='Чем занимается наше издание')
    address = models.TextField(blank=True, verbose_name='Юридический адрес издания')
    number_one = models.CharField(max_length=20, verbose_name='А1')
    number_two = models.CharField(max_length=20, verbose_name='МТС')
    number_three = models.CharField(max_length=20, verbose_name='Life')
    number_four = models.CharField(max_length=20, verbose_name='Городской телефон')
    email = models.EmailField
    location_map = models.ImageField(upload_to="photos_location_map/%Y/%m/%d", verbose_name='Схема проезда')






