# Generated by Django 2.2.1 on 2019-07-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('k', '0001_initial'), ('k', '0002_delete_person'), ('k', '0003_people'), ('k', '0004_auto_20190608_1514'), ('k', '0005_auto_20190613_0103'), ('k', '0006_auto_20190613_1747'), ('k', '0007_auto_20190614_1733'), ('k', '0008_auto_20190614_2047'), ('k', '0009_person_prix'), ('k', '0010_auto_20190624_0118'), ('k', '0011_auto_20190624_2351'), ('k', '0012_auto_20190625_1512'), ('k', '0013_auto_20190625_1545'), ('k', '0014_auto_20190703_1308')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(blank=True, max_length=30, null=True)),
                ('prenom', models.CharField(blank=True, max_length=30, null=True)),
                ('contact', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.CharField(blank=True, max_length=30, null=True)),
                ('domicile', models.CharField(blank=True, max_length=30, null=True)),
                ('modele', models.CharField(blank=True, max_length=40, null=True)),
                ('prix', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
    ]
