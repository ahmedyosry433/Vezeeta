# Generated by Django 3.2 on 2021-04-25 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_profile_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, choices=[('انف واذن وحنجرة', 'انف واذن وحنجرة'), ('جراحه سمنة ومناظير', 'جراحه سمنة ومناظير'), ('نفسي', 'نفسي'), ('جلدية', 'جلدية'), ('اورام', 'اورام'), ('قلب واوعية دموية', 'قلب واوعية دموية'), ('جراحة تجميل', 'جراحة تجميل'), ('مخ واعصاب', 'مخ واعصاب'), ('جراحة اوعية دموية', 'جراحة اوعية دموية'), ('عظام', 'عظام'), ('جراحة اطفال', 'جراحة اطفال'), ('نساء وتوليد', 'نساء وتوليد'), ('عيون', 'عيون'), ('امراض دم', 'امراض دم'), ('باطنه', 'باطنه'), ('جراحة اورام', 'جراحة اورام'), ('اسنان', 'اسنان'), ('اطفال حديثي الولادة', 'اطفال حديثي الولاد'), ('تخسيس وتغذية', 'تخسيس وتغذية')], max_length=50, null=True, verbose_name='دكتور ؟'),
        ),
    ]
