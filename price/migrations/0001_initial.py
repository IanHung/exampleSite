# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SimplePrice'
        db.create_table(u'price_simpleprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'price', ['SimplePrice'])

        # Adding model 'PackagePrice'
        db.create_table(u'price_packageprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'price', ['PackagePrice'])


    def backwards(self, orm):
        # Deleting model 'SimplePrice'
        db.delete_table(u'price_simpleprice')

        # Deleting model 'PackagePrice'
        db.delete_table(u'price_packageprice')


    models = {
        u'price.packageprice': {
            'Meta': {'object_name': 'PackagePrice'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'price.simpleprice': {
            'Meta': {'object_name': 'SimplePrice'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['price']