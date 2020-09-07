from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    # Additional
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username


class UserPro(models.Model):
    name = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    college = models.CharField(max_length=256)
    degree = models.CharField(max_length=256)
    course = models.CharField(max_length=256)
    passout = models.CharField(max_length=256)
    age = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_urls(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})
