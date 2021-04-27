# Generated by Django 3.2 on 2021-04-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_profile_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('قلب واوعية دموية', 'قلب واوعية دموية'), ('اورام', 'اورام'), ('باطنه', 'باطنه'), ('نفسي', 'نفسي'), ('اطفال حديثي الولادة', 'اطفال حديثي الولاد'), ('مخ واعصاب', 'مخ واعصاب'), ('نساء وتوليد', 'نساء وتوليد'), ('عيون', 'عيون'), ('جراحة اوعية دموية', 'جراحة اوعية دموية'), ('جراحه سمنة ومناظير', 'جراحه سمنة ومناظير'), ('جلدية', 'جلدية'), ('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('جراحة اطفال', 'جراحة اطفال'), ('جراحة تجميل', 'جراحة تجميل'), ('جراحة اورام', 'جراحة اورام'), ('تخسيس وتغذية', 'تخسيس وتغذية'), ('اسنان', 'اسنان'), ('امراض دم', 'امراض دم'), ('عظام', 'عظام')], max_length=50, null=True, verbose_name='دكتور ؟'),
        ),
    ]
