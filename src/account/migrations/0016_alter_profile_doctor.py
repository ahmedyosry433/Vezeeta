# Generated by Django 3.2 on 2021-04-29 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_profile_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('باطنه', 'باطنه'), ('نساء وتوليد', 'نساء وتوليد'), ('جراحة اوعية دموية', 'جراحة اوعية دموية'), ('جراحة تجميل', 'جراحة تجميل'), ('عيون', 'عيون'), ('اطفال حديثي الولادة', 'اطفال حديثي الولاد'), ('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('جراحة اورام', 'جراحة اورام'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('عظام', 'عظام'), ('جلدية', 'جلدية'), ('قلب واوعية دموية', 'قلب واوعية دموية'), ('امراض دم', 'امراض دم'), ('اورام', 'اورام'), ('اسنان', 'اسنان'), ('نفسي', 'نفسي'), ('جراحة اطفال', 'جراحة اطفال'), ('مخ واعصاب', 'مخ واعصاب'), ('جراحه سمنة ومناظير', 'جراحه سمنة ومناظير')], max_length=50, null=True, verbose_name='دكتور ؟'),
        ),
    ]
