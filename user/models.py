from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager (BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('email은 꼭 작성하여야합니다.')
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        if user.is_staff is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if user.is_superuser is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField('email', unique=True)
    name = models.CharField('이름', max_length=30, blank=False)
    is_superuser = models.BooleanField("최고관리자 권한", default=False)
    is_staff = models.BooleanField('관리자 권한', default=False)
    is_active = models.BooleanField('접속중', default=True)
    is_admin = models.BooleanField("admin", default=False)
    join_date = models.DateField('가입일자', default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'
