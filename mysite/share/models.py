from django.db import models
from django.contrib.auth.models import User


class ShareType(models.Model):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name


class Share(models.Model):
    photo = models.ImageField(upload_to='img', max_length=100)
    title = models.CharField(max_length=30)
    video = models.FileField(upload_to='vid', max_length=300, default='空')
    share_type = models.ForeignKey(ShareType, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    read_num = models.IntegerField(default=0)

    def __str__(self):
        return "<Share: %s>" % self.title

    class Meta:
        ordering = ['-read_num']
