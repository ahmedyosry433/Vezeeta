from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.utils.timezone import datetime
TYPE_OF_PERSON=(
    ('M',"Male"),
    ('F',"Female"),
)

class Profile (models.Model):
    DOCTOR_IN={
        ('جلدية',"جلدية"),
        ('اسنان',"اسنان"),
        ('نفسي',"نفسي"),
        ('اطفال حديثي الولادة',"اطفال حديثي الولاد"),
        ('مخ واعصاب',"مخ واعصاب"),
        ('عظام',"عظام"),
        ('نساء وتوليد',"نساء وتوليد"),
        ('انف واذن وحنجرة',"انف واذن وحنجرة"),
        ('قلب واوعية دموية',"قلب واوعية دموية"),
        ('امراض دم',"امراض دم"),
        ('اورام',"اورام"),
        ('باطنه',"باطنه"),
        ('تخسيس وتغذية',"تخسيس وتغذية"),
        ('جراحة اطفال',"جراحة اطفال"),
        ('جراحة اورام',"جراحة اورام"),
        ('جراحة اوعية دموية',"جراحة اوعية دموية"),
        ('جراحة تجميل',"جراحة تجميل"),
        ('جراحه سمنة ومناظير',"جراحه سمنة ومناظير"),
        ('عيون',"عيون")

    }

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("الاسم :"), max_length=80)
    subtitle = models.CharField(_("نبذه عنك :"), max_length=50)
    adresss = models.CharField(_("المحافظه :"), max_length=50)
    adresss_detail = models.CharField(_("العنوان بالتفاصيل :"), max_length=50)
    number_phone = models.CharField(_("الهاتف :"), max_length=30)
    working_hours = models.IntegerField(_("عدد ساعات العمل :"), blank=True, null=True)
    wating_time = models.IntegerField(_("مده الانتظار :"), blank=True, null=True)
    who_i = models.TextField(_("من انت"), max_length=250, blank=True, null=True)
    price = models.IntegerField(_("السعر :"), blank=True, null=True)
    img = models.ImageField(_("الصوره الشخصيه"),upload_to='profail', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True , null= True)
    twitter = models.CharField(max_length=100, blank=True , null= True)
    google = models.CharField(max_length=100, blank=True , null= True)
    type_of_person = models.CharField(max_length=20,choices=TYPE_OF_PERSON , blank=True , null=True)
    join_now = models.DateTimeField(auto_now=False, auto_now_add=True)
    doctor = models.CharField(_("دكتور ؟"),choices=DOCTOR_IN, max_length=50, blank=True, null=True)
    specialist_doctor = models.CharField(_("متخصص في ؟"), max_length=100, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            Profile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile, sender=User)
