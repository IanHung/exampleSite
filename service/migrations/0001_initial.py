# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'service_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('intro', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'service', ['Service'])

        # Adding model 'Paragraph'
        db.create_table(u'service_paragraph', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Service'])),
            ('paragraphPosition', self.gf('django.db.models.fields.IntegerField')()),
            ('paragraph', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'service', ['Paragraph'])


    def backwards(self, orm):
        # Deleting model 'Service'
        db.delete_table(u'service_service')

        # Deleting model 'Paragraph'
        db.delete_table(u'service_paragraph')


    models = {
        u'service.paragraph': {
            'Meta': {'object_name': 'Paragraph'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paragraph': ('django.db.models.fields.TextField', [], {}),
            'paragraphPosition': ('django.db.models.fields.IntegerField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['service.Service']"})
        },
        u'service.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['service']