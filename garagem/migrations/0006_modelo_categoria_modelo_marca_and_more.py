# Generated by Django 4.1.7 on 2023-04-28 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0005_modelo"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelo",
            name="categoria",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="garagem.categoria",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="modelo",
            name="marca",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="garagem.marca",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="veiculo",
            name="categoria",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="garagem.categoria"
            ),
        ),
        migrations.AlterField(
            model_name="veiculo",
            name="cor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="garagem.cor"
            ),
        ),
        migrations.AlterField(
            model_name="veiculo",
            name="marca",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="garagem.marca"
            ),
        ),
    ]
