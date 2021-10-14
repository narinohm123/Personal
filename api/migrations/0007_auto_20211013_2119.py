# Generated by Django 3.2.8 on 2021-10-13 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='religion',
        ),
        migrations.AddField(
            model_name='profile',
            name='religion_con',
            field=models.CharField(blank=True, choices=[('คณบดี', 'คณบดี'), ('รองคณบดี', 'รองคณบดี'), ('ผู้ช่วยคณบดี', 'ผู้ช่วยคณบดี'), ('ประธานหลักสูตร', 'ประธานหลักสูตร'), ('หัวหน้างาน', 'หัวหน้างาน')], max_length=100, null=True),
        ),
    ]