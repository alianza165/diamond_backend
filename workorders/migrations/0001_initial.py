# Generated by Django 5.1.7 on 2025-03-27 09:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Closed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Machine_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Part_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Type_of_Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_work', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.CharField(max_length=50)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorders.location')),
                ('machine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorders.machine_type')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=50)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorders.equipment')),
                ('part_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorders.part_type')),
            ],
        ),
        migrations.CreateModel(
            name='workorders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('department', models.CharField(choices=[('Electrical', 'ELECTRICAL'), ('Mechanical', 'MECHANICAL'), ('Miscellaneous', 'MISCELLANEOUS')], default='miscellaneous', max_length=20)),
                ('problem', models.TextField()),
                ('closing_remarks', models.TextField(blank=True, null=True)),
                ('accepted', models.BooleanField(default=None, null=True)),
                ('assigned_to', models.CharField(blank=True, max_length=100, null=True)),
                ('target_date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('replaced_part', models.CharField(default='none', max_length=50)),
                ('completion_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pr_number', models.CharField(default='none', max_length=50)),
                ('pr_date', models.DateTimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('closed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workorders.closed')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorders.equipment')),
                ('initiated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('part', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='workorders.part')),
                ('pending', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workorders.pending')),
                ('type_of_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorders.type_of_work')),
                ('work_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workorders.work_status')),
            ],
        ),
    ]
