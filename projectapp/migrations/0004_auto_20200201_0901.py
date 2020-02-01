# Generated by Django 2.2 on 2020-02-01 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0003_stdnotice_stdsubjectlist_teacherform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stdsubjectentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectnameentry', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='stdsubjectlist',
            old_name='subjectname',
            new_name='subjectcode',
        ),
        migrations.AddField(
            model_name='stdsubjectlist',
            name='stdsubjectentry',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stdsubjectlist', to='projectapp.Stdsubjectentry'),
            preserve_default=False,
        ),
    ]