# Generated by Django 3.0.8 on 2020-09-06 07:37

from django.db import migrations, models
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='최고관리자 권한')),
                ('is_staff', models.BooleanField(default=False, verbose_name='관리자 권한')),
                ('is_active', models.BooleanField(default=True, verbose_name='접속중')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('join_date', models.DateField(default=django.utils.timezone.now, verbose_name='가입일자')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]