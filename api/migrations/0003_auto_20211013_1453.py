# Generated by Django 3.2.7 on 2021-10-13 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_approval_budget_budget_con_degree_document_event_event_connect_faculty_human_resource_human_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]