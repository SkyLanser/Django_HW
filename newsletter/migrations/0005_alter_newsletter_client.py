# Generated by Django 4.2.6 on 2023-10-31 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_alter_newsletter_end_alter_newsletter_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='client',
            field=models.ManyToManyField(to='newsletter.client', verbose_name='Клиенты'),
        ),
    ]
