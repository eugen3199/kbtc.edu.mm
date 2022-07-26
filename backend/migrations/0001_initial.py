# Generated by Django 3.2.7 on 2021-11-24 10:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtaildocs', '0012_uploadeddocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degreeName', models.CharField(max_length=50, verbose_name='Degree Name')),
            ],
            options={
                'verbose_name': 'Academic Degree',
                'verbose_name_plural': 'Academic Degrees',
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusName', models.CharField(max_length=200, verbose_name='Campus Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('query', models.TextField(verbose_name='Query for Google Map')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campuses',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTitle', models.CharField(max_length=100, verbose_name='Course Title')),
                ('overview', wagtail.core.fields.RichTextField(verbose_name='Course Overview')),
                ('courseDocument', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courseDocument', to='wagtaildocs.document')),
                ('coursePhoto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courseImage', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelName', models.CharField(max_length=50, verbose_name='Level')),
            ],
            options={
                'verbose_name': 'Level',
                'verbose_name_plural': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(max_length=100, verbose_name='School Name')),
                ('schoolContact', wagtail.core.fields.StreamField([('Email', wagtail.core.blocks.StructBlock([('email', wagtail.core.blocks.EmailBlock(help_text='Enter Email'))])), ('Phone', wagtail.core.blocks.StructBlock([('phone', wagtail.core.blocks.CharBlock(help_text='Enter Phone Number', validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '09123456789'.", regex='^09\\d{7,9}$')]))]))])),
                ('missions', wagtail.core.fields.RichTextField(verbose_name='Enter missions')),
                ('facebookLink', models.URLField(verbose_name='Enter Facebook link')),
                ('linkedinLink', models.URLField(verbose_name='Enter Linkedin link')),
                ('youtubeLink', models.URLField(verbose_name='Enter Youtube link')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitTitle', models.CharField(max_length=100, verbose_name='Unit Title')),
                ('overview', wagtail.core.fields.RichTextField(verbose_name='Unit Overview')),
                ('coverPhoto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unitImages', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
        migrations.CreateModel(
            name='SchoolCampusRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('campusName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.campus')),
                ('schoolName', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_campus', to='backend.schoolinfo')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255, verbose_name='Caption')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='CourseUnitRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('Unit_Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.unit')),
                ('courseName', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_unit', to='backend.course')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='level_Name', to='backend.levels'),
        ),
        migrations.CreateModel(
            name='AcademicCourseRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='backend.course')),
                ('degreeName', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_course', to='backend.academic')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='academic',
            name='school',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='school_Name', to='backend.schoolinfo'),
        ),
    ]
