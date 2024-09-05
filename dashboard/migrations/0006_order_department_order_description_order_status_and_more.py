# Generated by Django 4.2.11 on 2024-04-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_order_id_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='department',
            field=models.CharField(choices=[('IT', 'IT'), ('FAD', 'FAD'), ('SECURITY', 'SECURITY')], max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(choices=[('IT', 'IT'), ('FAD', 'FAD'), ('SECURITY', 'SECURITY')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_cost',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
