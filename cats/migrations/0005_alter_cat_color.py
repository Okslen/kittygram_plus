# Generated by Django 3.2 on 2022-08-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_rename_achievements_achievementcat_achievement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]