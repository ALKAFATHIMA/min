# Generated by Django 5.0.2 on 2024-05-14 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashaease', '0010_children'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pregnant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancy_months', models.IntegerField(default=0)),
                ('month1_weight', models.BooleanField(default=False)),
                ('month1_bp', models.BooleanField(default=False)),
                ('month1_hr', models.BooleanField(default=False)),
                ('month2_weight', models.BooleanField(default=False)),
                ('month2_bp', models.BooleanField(default=False)),
                ('month2_hr', models.BooleanField(default=False)),
                ('month3_weight', models.BooleanField(default=False)),
                ('month3_bp', models.BooleanField(default=False)),
                ('month3_hr', models.BooleanField(default=False)),
                ('month4_weight', models.BooleanField(default=False)),
                ('month4_bp', models.BooleanField(default=False)),
                ('month4_hr', models.BooleanField(default=False)),
                ('month5_weight', models.BooleanField(default=False)),
                ('month5_bp', models.BooleanField(default=False)),
                ('month5_hr', models.BooleanField(default=False)),
                ('month6_weight', models.BooleanField(default=False)),
                ('month6_bp', models.BooleanField(default=False)),
                ('month6_hr', models.BooleanField(default=False)),
                ('month7_weight', models.BooleanField(default=False)),
                ('month7_bp', models.BooleanField(default=False)),
                ('month7_hr', models.BooleanField(default=False)),
                ('month8_weight', models.BooleanField(default=False)),
                ('month8_bp', models.BooleanField(default=False)),
                ('month8_hr', models.BooleanField(default=False)),
                ('month9_weight', models.BooleanField(default=False)),
                ('month9_bp', models.BooleanField(default=False)),
                ('month9_hr', models.BooleanField(default=False)),
                ('month10_weight', models.BooleanField(default=False)),
                ('month10_bp', models.BooleanField(default=False)),
                ('month10_hr', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ashaease.members')),
            ],
        ),
    ]