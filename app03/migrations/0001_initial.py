# Generated by Django 2.2.4 on 2020-03-02 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='名字')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('pwd', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
    ]