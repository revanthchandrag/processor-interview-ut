# Generated by Django 4.2.16 on 2024-09-22 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=100)),
                ('card_number', models.CharField(max_length=16)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit'), ('Transfer', 'Transfer')], max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('target_card_number', models.CharField(blank=True, max_length=16, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]