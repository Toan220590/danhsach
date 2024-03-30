# Generated by Django 4.1 on 2024-03-30 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('ten', models.CharField(max_length=250)),
                ('bien_so', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Nhan_vien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay_tao', models.DateTimeField(auto_now_add=True)),
                ('ten', models.CharField(max_length=250)),
                ('xe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DANHSACH.xe')),
            ],
        ),
    ]
