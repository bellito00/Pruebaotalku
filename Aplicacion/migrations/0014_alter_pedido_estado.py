# Generated by Django 5.0.6 on 2024-07-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0013_alter_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('Cancelado', 'Cancelado'), ('Entregado', 'Entregado'), ('En circulacion', 'En circulacion'), ('Pagado', 'Pagado')], default='Pagado', max_length=50),
        ),
    ]
