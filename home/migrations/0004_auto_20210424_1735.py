# Generated by Django 3.0.8 on 2021-04-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210407_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='interludesslot',
            name='color',
            field=models.CharField(choices=[('a', 'Bleu foncé'), ('b', 'Rouge'), ('c', 'Jaune'), ('d', 'Bleu'), ('e', 'Vert'), ('f', 'Noir'), ('g', 'Orange')], default='a', max_length=1, verbose_name='Couleur'),
        ),
        migrations.AlterField(
            model_name='interludesactivity',
            name='description',
            field=models.TextField(help_text='Texte ou html selon la valeur de "Description HTML".\n', max_length=10000, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='interludesactivity',
            name='host_email',
            field=models.EmailField(help_text='Utilisé pour communiquer la liste des participants si demandé', max_length=254, verbose_name="email de l'organisateur"),
        ),
        migrations.AlterField(
            model_name='interludesactivity',
            name='host_name',
            field=models.CharField(blank=True, help_text='Peut-être laissé vide pour des simples activités sans orga', max_length=50, null=True, verbose_name="nom de l'organisateur"),
        ),
    ]
