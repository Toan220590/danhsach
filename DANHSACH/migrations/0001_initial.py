# Generated by Django 4.1 on 2024-05-17 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capnhat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trang_thai', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='So_dien_thoai_gui',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdtg', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='So_dien_thoai_nhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdtn', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tin_nhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('tin_nhan', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Xe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('ten_xe', models.CharField(max_length=250)),
                ('bien_so', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Nhan_vien_xe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('seri', models.CharField(max_length=250)),
                ('ten_nhan_vien', models.CharField(max_length=250)),
                ('xe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DANHSACH.xe')),
            ],
        ),
        migrations.CreateModel(
            name='Nhan_vien',
            fields=[
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('seri', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('ten_nhan_vien', models.CharField(max_length=250)),
                ('nam_sinh', models.CharField(max_length=250)),
                ('cccd', models.CharField(max_length=250)),
                ('xe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DANHSACH.xe')),
            ],
        ),
    ]
