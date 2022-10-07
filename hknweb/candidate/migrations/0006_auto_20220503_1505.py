# Generated by Django 2.2.8 on 2022-05-03 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0005_auto_20220421_0027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateformdoneentry',
            name='form',
        ),
        migrations.RemoveField(
            model_name='candidateformdoneentry',
            name='users',
        ),
        migrations.RemoveField(
            model_name='committeeproject',
            name='candidateSemesterActive',
        ),
        migrations.RemoveField(
            model_name='committeeprojectdoneentry',
            name='committeeProject',
        ),
        migrations.RemoveField(
            model_name='committeeprojectdoneentry',
            name='users',
        ),
        migrations.RemoveField(
            model_name='duepayment',
            name='candidateSemesterActive',
        ),
        migrations.RemoveField(
            model_name='duepaymentpaidentry',
            name='duePayment',
        ),
        migrations.RemoveField(
            model_name='duepaymentpaidentry',
            name='users',
        ),
        migrations.RemoveField(
            model_name='mergeeventsmultiplierentry',
            name='eventType',
        ),
        migrations.RemoveField(
            model_name='mergeeventsmultiplierentry',
            name='requirementMergeRequirement',
        ),
        migrations.RemoveField(
            model_name='requirementbitbyteactivity',
            name='candidateSemesterActive',
        ),
        migrations.RemoveField(
            model_name='requirementhangout',
            name='candidateSemesterActive',
        ),
        migrations.RemoveField(
            model_name='requirementmandatory',
            name='candidateSemesterActive',
        ),
        migrations.RemoveField(
            model_name='requirementmandatory',
            name='events',
        ),
        migrations.RemoveField(
            model_name='requirementmergerequirement',
            name='candidateSemesterActive',
        ),
        migrations.RemoveField(
            model_name='requriementevent',
            name='candidateSemesterActive',
        ),
        migrations.RemoveField(
            model_name='requriementevent',
            name='eventType',
        ),
        migrations.DeleteModel(
            name='CandidateForm',
        ),
        migrations.DeleteModel(
            name='CandidateFormDoneEntry',
        ),
        migrations.DeleteModel(
            name='CommitteeProject',
        ),
        migrations.DeleteModel(
            name='CommitteeProjectDoneEntry',
        ),
        migrations.DeleteModel(
            name='DuePayment',
        ),
        migrations.DeleteModel(
            name='DuePaymentPaidEntry',
        ),
        migrations.DeleteModel(
            name='MergeEventsMultiplierEntry',
        ),
        migrations.DeleteModel(
            name='RequirementBitByteActivity',
        ),
        migrations.DeleteModel(
            name='RequirementHangout',
        ),
        migrations.DeleteModel(
            name='RequirementMandatory',
        ),
        migrations.DeleteModel(
            name='RequirementMergeRequirement',
        ),
        migrations.DeleteModel(
            name='RequriementEvent',
        ),
    ]