from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from hitcount.models import HitCount

from django.utils import timezone

# IP-адрес и количество посещений сайта
class Userip(models.Model):
    ip=models.CharField(verbose_name='Айпи адрес',max_length=30)    #айпи адрес
    count=models.IntegerField(verbose_name='Визиты',default=0) # Ip посещения
    class Meta:
        verbose_name = 'Доступ к информации о пользователе'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.ip

# Всего посещений сайта
class VisitNumber(models.Model):
    count=models.IntegerField(verbose_name='Всего посещений сайта',default=0) # Всего посещений сайта
    class Meta:
        verbose_name = 'Всего посещений сайта'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.count)

# Статистика посещений за один день
class DayNumber(models.Model):
    day=models.DateField(verbose_name='свидание',default=timezone.now)
    count=models.IntegerField(verbose_name='Количество посещений сайта',default=0) # Всего посещений сайта
    class Meta:
        verbose_name = 'Статистика ежедневных посещений сайта'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.day)








class MarPage(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Maruza'

    def __str__(self):
        return self.title


class Maruza(models.Model):
    file = models.FileField()
    page = models.ForeignKey(MarPage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.file)


class AmaPage(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Amaliyot'

    def __str__(self):
        return self.nomi


class Amaliyot(models.Model):
    # nomi = models.CharField(max_length=100)
    file = models.FileField()
    page = models.ForeignKey(AmaPage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.file)


class LabPage(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Labaratoriya'

    def __str__(self):
        return self.nomi


class Labartoriya(models.Model):
    # nomi = models.CharField(max_length=100)
    file = models.FileField()
    page = models.ForeignKey(LabPage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name_plural = 'Labartoriya'


class MusPage(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Mustaqil talim'

    def __str__(self):
        return self.nomi


class MustaqilTalim(models.Model):
    # nomi = models.CharField(max_length=100)
    file = models.FileField()
    page = models.ForeignKey(MusPage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name_plural = 'MustaqilTalim'


class ScopPage(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Scopsus'

    def __str__(self):
        return self.nomi


class Scopus(models.Model):
    # nomi = models.CharField(max_length=100)
    file = models.FileField()
    page = models.ForeignKey(ScopPage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name_plural = 'Scopus'


class OakPage(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'OAK'

    def __str__(self):
        return self.nomi


class OAK(models.Model):
    # nomi = models.CharField(max_length=100)
    file = models.FileField()
    page = models.ForeignKey(OakPage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name_plural = 'OAK'


class KonfPage(models.Model):
    nomi = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Konfiresnsiya'

    def __str__(self):
        return self.nomi


class Konfirensiya(models.Model):
    # nomi = models.CharField(max_length=100)
    file = models.FileField()
    page = models.ForeignKey(KonfPage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.file)

    class Meta:
        verbose_name_plural = 'Konfirensiya'
