# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings

UNIQUE_EMAIL = getattr(settings, 'ACCOUNT_UNIQUE_EMAIL', True)
UNIQUE_EMAIL_MULTISITE = getattr(settings, 'ACCOUNT_UNIQUE_EMAIL_MULTISITE', False)


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('account', '0002_email_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailaddress',
            name='site',
            field=models.ForeignKey(default=1, to='sites.Site'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='email',
            field=models.EmailField(unique=not(UNIQUE_EMAIL and UNIQUE_EMAIL_MULTISITE),
                                    max_length=254, verbose_name='e-mail address'),
            preserve_default=True,
        ),
    ]

    if UNIQUE_EMAIL_MULTISITE:
       operations += [
           migrations.AlterUniqueTogether(
            name='emailaddress',
            unique_together=set([('email', 'site')]),
        ),
       ]
