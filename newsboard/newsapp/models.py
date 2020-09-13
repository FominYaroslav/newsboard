from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin

# from django.contrib.auth.models import User

from .manager import UserManager

# class User(User):


class User(AbstractBaseUser, PermissionsMixin):
    username = models.fields.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    object = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @classmethod
    def get_default_user(cls):
        user, created = cls.object.get_or_create(username="Anonymus")
        return user.pk


class News(models.Model):
    title = models.fields.CharField(max_length=40)
    link = models.fields.TextField()
    creation_date = models.fields.DateField(auto_now=True)
    author = models.ForeignKey(
        User,
        related_name="news_author",
        default=User.get_default_user,
        on_delete=models.SET_DEFAULT,
    )
    upvoted = models.ManyToManyField(User, related_name="news_upvoted", blank=True)

    @property
    def amount_of_upvotes(self):
        return len(self.upvoted.all())

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.fields.TextField()
    creation_date = models.fields.DateField(auto_now=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, default=User.get_default_user, on_delete=models.SET_DEFAULT
    )

    def __str__(self):
        return f"Comment to {self.content[:10]}"
