# Generated by Django 2.0.7 on 2018-09-22 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pontuacoes', '0004_auto_20180922_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividadealuno',
            name='aluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Aluno'),
        ),
        migrations.AlterField(
            model_name='atividadealuno',
            name='atividade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pontuacoes.Atividade'),
        ),
    ]
