# Generated by Django 3.2 on 2021-04-26 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HazenaIS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kariera',
            old_name='hrac_hID',
            new_name='hrac',
        ),
        migrations.RenameField(
            model_name='kariera',
            old_name='klub_kID',
            new_name='klub',
        ),
        migrations.RenameField(
            model_name='kariera',
            old_name='sezona_sID',
            new_name='sezona',
        ),
        migrations.RenameField(
            model_name='vysledky',
            old_name='klub_kID',
            new_name='klub',
        ),
        migrations.RenameField(
            model_name='vysledky',
            old_name='sezona_sID',
            new_name='sezona',
        ),
        migrations.RenameField(
            model_name='zapasy',
            old_name='domaci_ID',
            new_name='domaci',
        ),
        migrations.RenameField(
            model_name='zapasy',
            old_name='hoste_ID',
            new_name='hoste',
        ),
        migrations.RenameField(
            model_name='zapasy',
            old_name='rozhodci_rID',
            new_name='rozhodci',
        ),
        migrations.RenameField(
            model_name='zapiszapasu',
            old_name='hrac_hID',
            new_name='hrac',
        ),
        migrations.RenameField(
            model_name='zapiszapasu',
            old_name='zapasy_zID',
            new_name='zapasy',
        ),
    ]
