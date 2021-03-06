# Generated by Django 3.2.8 on 2021-10-14 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20211013_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id_degree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.degree'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion_con',
            field=models.CharField(blank=True, choices=[('พุทธ', 'พุทธ'), ('คริสต์', 'คริสต์'), ('อิสลาม', 'อิสลาม'), ('ยิว', 'ยิว'), ('ซิกข์', 'ซิกข์'), ('บาไฮ', 'บาไฮ'), ('โซโรอัสเตอร์', 'โซโรอัสเตอร์'), ('พราหมณ์-ฮินดู', 'พราหมณ์-ฮินดู'), ('เชน', 'เชน'), ('ไม่มีศาสนา', 'ไม่มีศาสนา')], max_length=100, null=True),
        ),
    ]
