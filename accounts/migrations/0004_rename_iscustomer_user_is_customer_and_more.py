# Generated by Django 4.1.3 on 2023-02-23 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_user_phone_number_seller_customer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="isCustomer",
            new_name="is_customer",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="isSeller",
            new_name="is_seller",
        ),
    ]