from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    writer = models.ForeignKey(User, on_delete=models.CASCADE) # 유저와 게시글이 1:N의 관계이기 때문에 게시글 쪽에서 합침.
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    #on_delete: user가 탈퇴할 때 어떻게 처리할 것인가.
    #1.게시글도 같이 지운다
    #2.유저를 null값 처리
