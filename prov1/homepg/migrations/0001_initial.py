# Generated by Django 2.1.6 on 2019-02-17 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=20)),
                ('store_name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepg.Vendor'),
        ),
    ]
