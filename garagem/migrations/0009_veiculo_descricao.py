# Generated by Django 4.1.7 on 2023-06-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0008_veiculo_modelo"),
    ]

    operations = [
        migrations.AddField(
            model_name="veiculo",
            name="descricao",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]