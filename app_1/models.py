from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from django import forms


class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    clas = models.IntegerField(null=True, blank=True)


class SClass(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='классы', max_length=256, blank=True)


    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'классы'


class Lesson(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='наименование предмета', max_length=256, blank=True)

    class Meta:
        verbose_name = 'наименование предмета'
        verbose_name_plural = 'наименование предметов'


class Time(models.Model):
    def __str__(self):
        return self.time

    time = models.CharField(verbose_name='промежутки времени', max_length=256, blank=True)

    class Meta:
        verbose_name = 'промежуток времени'
        verbose_name_plural = 'промежутки времени'


class Schedule(models.Model):

    class_id = models.ForeignKey(SClass, on_delete=models.PROTECT, verbose_name='номер класса')
    lesson_id = models.ForeignKey(Lesson, on_delete=models.PROTECT, verbose_name='ID урока')
    time_id = models.ForeignKey(Time, on_delete=models.PROTECT, verbose_name='Время')
    week_day = models.IntegerField(null=True, blank=True, verbose_name='День недели_цифрой')

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'


class Ways(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(verbose_name='Направления', max_length=256, blank=True)


    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'


class Registration(models.Model):

    first_name = models.CharField('Имя ребёнка', max_length=70)
    last_name = models.CharField('Фамилия ребёнка', max_length=70, blank=True)
    age = models.IntegerField('Возраст', validators=[MinValueValidator(6), MaxValueValidator(18)])
    about = models.TextField('Увлечения ребенка', max_length=200)
    way = models.ForeignKey(Ways, on_delete=models.PROTECT, verbose_name='Направление')
    email = models.EmailField('Электронная почта')
    phoneNumberRegex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    phone_number = models.CharField('Номер телефона', validators=[phoneNumberRegex], max_length=16, unique=True)

    class Meta:
        verbose_name = 'регистрация'
        verbose_name_plural = 'регистрации'