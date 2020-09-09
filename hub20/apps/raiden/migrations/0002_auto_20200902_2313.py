# Generated by Django 3.1 on 2020-09-02 23:13

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models

import hub20.apps.ethereum_money.models


class Migration(migrations.Migration):

    dependencies = [
        ("blockchain", "0001_initial"),
        ("ethereum_money", "0001_initial"),
        ("raiden", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceDeposit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "amount",
                    hub20.apps.ethereum_money.models.EthereumTokenAmountField(
                        decimal_places=18, max_digits=32
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ethereum_money.ethereumtoken",
                    ),
                ),
                (
                    "raiden",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="raiden.raiden"
                    ),
                ),
                (
                    "transaction",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="blockchain.transaction"
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]