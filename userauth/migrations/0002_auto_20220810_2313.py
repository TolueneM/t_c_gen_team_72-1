# Generated by Django 3.2.15 on 2022-08-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicyQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_policyUseChoice', models.CharField(max_length=50)),
                ('construction', models.BooleanField(null=True)),
                ('finance', models.BooleanField(null=True)),
                ('employment', models.BooleanField(null=True)),
                ('freelancer', models.BooleanField(null=True)),
                ('health_care', models.BooleanField(null=True)),
                ('saas', models.BooleanField(null=True)),
                ('entertainment', models.BooleanField(null=True)),
                ('userCreateAccount', models.BooleanField()),
                ('websiteOffer', models.BooleanField()),
                ('other_personalInfo', models.CharField(max_length=50)),
                ('collectPersonalInfo', models.BooleanField()),
                ('marketingCommnuication', models.BooleanField()),
                ('acceptPayments', models.BooleanField()),
                ('containAds', models.BooleanField()),
                ('upPostContent', models.BooleanField()),
                ('disclosePerInfo', models.BooleanField()),
                ('discloseCollectInfo', models.BooleanField()),
                ('secureMeausre', models.BooleanField()),
                ('provideService', models.BooleanField(null=True)),
                ('provideEmailAdd', models.CharField(max_length=50, null=True)),
                ('legalName', models.CharField(max_length=200, null=True)),
                ('tradeNameBusiness', models.BooleanField(null=True)),
                ('companyEmail', models.CharField(max_length=50, null=True)),
                ('phoneNumber', models.IntegerField(null=True)),
                ('fax', models.IntegerField(null=True)),
                ('compAddressLine', models.CharField(max_length=200)),
                ('cityTown', models.CharField(max_length=150)),
                ('zipCode', models.IntegerField()),
                ('versionDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Terms_and_condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('tnc_or_policy', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
            options={
                'db_table': 't_C',
            },
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='company',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='contactNumber',
            field=models.IntegerField(default=23480000000),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='userAddress',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
