# from django.contrib.contenttypes.models import ContentType
# from django.db import models
# from django.conf import settings
# from django.contrib.auth.models import User
# from publications.models import Publications


# class Comment(models.Model):
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор комментария', on_delete=models.CASCADE)
#     text_comment = models.TextField(verbose_name='Текст комментария', )
#     parent = models.ForeignKey(
#         'self',
#         verbose_name='Комментарий-родитель',
#         blank=True,
#         null=True,
#         related_name='comment_children',
#         on_delete=models.CASCADE
#     )
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     time_create = models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')
#
#     def __str__(self):
#         return self.id


# class LikeDisLike(models.Model):
#     pass
