# -*- coding: utf-8 -*-

from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=256)
    dob = models.DateField("Date of birth")

    def __unicode__(self):
        return self.name


class MusicianPerformance(models.Model):

    INSTRUMENTS = (
        (u'rebab', u'Rebab'),
        (u'gender', u'Gendèr'),
        (u'gender-panerus', u'Gendèr Panerus'),
        (u'gambang', u'Gambang'),
        (u'slenthem', u'Slenthem'),
        (u'bonang', u'Bonang Barung'),
        (u'bonang-panerus', u'Bonang Panerus'),
        (u'kenong', u'Kenong'),
        (u'gong', u'Gong'),
        (u'siter', u'Siter'),
        (u'celempung', u'Celempung'),
        (u'suling', u'Suling'),
        (u'gerong', u'Gerong'),
        (u'sindhen', u'Sindhèn'),
    )
    musician = models.ForeignKey(Musician)
    instrument = models.CharField(max_length=256, choices=INSTRUMENTS)

    def __unicode__(self):
        return u"%s plays %s" % (self.musician, self.instrument)
