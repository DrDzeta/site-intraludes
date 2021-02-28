# Generated by Django 3.0.8 on 2021-02-28 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterludesActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('duration', models.DurationField(verbose_name='Durée')),
                ('host_name', models.CharField(max_length=50, verbose_name="Nom de l'organisateur")),
                ('host_email', models.EmailField(max_length=254, verbose_name="Email de l'organisateur")),
                ('description', models.TextField(max_length=2000, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='InterludesParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom complet')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('school', models.CharField(choices=[('U', 'ENS Ulm'), ('L', 'ENS Lyon'), ('R', 'ENS Rennes'), ('C', 'ENS Paris Saclay')], max_length=1, verbose_name='ENS de rattachement')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Utilisateur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveIntegerField()),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.InterludesActivity')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.InterludesParticipant')),
            ],
            options={
                'unique_together': {('priority', 'participant')},
            },
        ),
    ]
