# Generated by Django 2.1.5 on 2019-01-08 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('ASE', 'Associate Software Engineer'), ('SE', 'Software Engineer'), ('SSE', 'Senior Software Engineer'), ('TL', 'Team Lead'), ('SA', 'System Analyst'), ('PM', 'Project Manager')], max_length=3)),
                ('tech', models.CharField(choices=[('PY', 'Python'), ('PHP', 'PHP'), ('JAVA', 'Java'), ('JS', 'JavaScript')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dev', to='emp.Employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.Project')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pm', to='emp.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='on_projects',
            field=models.ManyToManyField(to='emp.Project'),
        ),
    ]
