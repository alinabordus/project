from django.db import models

# Create your models here.
class Post(models.Model):
    '''данные о посте'''
    tittle = models.CharField('Заголовок запису', max_length=100)
    description = models.TextField('Текст запису')
    author = models.CharField('Імя автора', max_length=100)
    date = models.DateField('Дата публікації')
    img = models.ImageField('Зображення', upload_to='image/%Y')


    def __str__(self):
        return f'{self.tittle}.{self.author}'
    
    
    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    '''Коментар'''
    email = models.EmailField()
    name = models.CharField('Імя', max_length=50)
    text_comments = models.TextField('Текст коментаря', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}.{self.post}'
    
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'


class Likes(models.Model):
    '''лайки'''
    ip = models.CharField('IP-адреса', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)
    
