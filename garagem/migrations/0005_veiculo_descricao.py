# Generated by Django 4.2.1 on 2023-05-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0004_alter_acessorio_options_alter_veiculo_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="veiculo",
            name="descricao",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]