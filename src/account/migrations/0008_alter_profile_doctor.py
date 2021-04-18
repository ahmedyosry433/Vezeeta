# Generated by Django 3.2 on 2021-04-16 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_profile_working_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('جراحة اطفال', 'جراحة اطفال'), ('باطنه', 'باطنه'), ('جراحة تجميل', 'جراحة تجميل'), ('جراحة اوعية دموية', 'جراحة اوعية دموية'), ('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('جلدية', 'جلدية'), ('جراحة اورام', 'جراحة اورام'), ('قلب واوعية دموية', 'قلب واوعية دموية'), ('اورام', 'اورام'), ('نساء وتوليد', 'نساء وتوليد'), ('اطفال حديثي الولادة', 'اطفال حديثي الولاد'), ('نفسي', 'نفسي'), ('مخ واعصاب', 'مخ واعصاب'), ('اسنان', 'اسنان'), ('امراض دم', 'امراض دم'), ('عظام', 'عظام'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('جراحه سمنة ومناظير', 'جراحه سمنة ومناظير')], max_length=50, null=True, verbose_name='دكتور ؟'),
        ),
    ]
