from django.db import models

from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자',
    )
    photo = models.ImageField('사진', upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = f'{verbose_name} 목록'
        ordering = ['-pk']



class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='포스트',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )
    content = models.TextField('댓글 내용')
    tags = models.ManyToManyField(
        'HashTag',
        blank=True,
        verbose_name='해쉬태그'
    )

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = f'{verbose_name} 목록'

class HashTag(models.Model):
    name = models.CharField('태그명', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '해쉬태그'
        verbose_name_plural = f'{verbose_name} 목록'