# Generated by Django 4.2.4 on 2023-08-16 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('order_status', models.CharField(choices=[('received', 'Received'), ('preparing', 'Preparing'), ('ready', 'Ready for Pickup'), ('delivered', 'Delivered')], default='received', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.dish')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(through='zomato.OrderDish', to='zomato.dish'),
        ),
    ]
