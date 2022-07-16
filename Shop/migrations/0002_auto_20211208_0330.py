# Generated by Django 3.2.5 on 2021-12-07 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('item_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to=settings.AUTH_USER_MODEL)),
                ('item_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.product')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_product',
            field=models.ManyToManyField(to='Shop.OrderProduct'),
        ),
    ]