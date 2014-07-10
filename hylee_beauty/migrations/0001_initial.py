# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manufacturer'
        db.create_table(u'hylee_beauty_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'hylee_beauty', ['Manufacturer'])

        # Adding model 'Category'
        db.create_table(u'hylee_beauty_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hylee_beauty.Category'])),
            ('top', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'hylee_beauty', ['Category'])

        # Adding model 'Image'
        db.create_table(u'hylee_beauty_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'hylee_beauty', ['Image'])

        # Adding model 'Product'
        db.create_table(u'hylee_beauty_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=100000)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ean', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('date_available', self.gf('django.db.models.fields.DateField')()),
            ('date_import', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')()),
            ('dimension_length', self.gf('django.db.models.fields.FloatField')()),
            ('dimension_height', self.gf('django.db.models.fields.FloatField')()),
            ('dimension_width', self.gf('django.db.models.fields.FloatField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hylee_beauty.Manufacturer'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hylee_beauty.Category'])),
        ))
        db.send_create_signal(u'hylee_beauty', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Manufacturer'
        db.delete_table(u'hylee_beauty_manufacturer')

        # Deleting model 'Category'
        db.delete_table(u'hylee_beauty_category')

        # Deleting model 'Image'
        db.delete_table(u'hylee_beauty_image')

        # Deleting model 'Product'
        db.delete_table(u'hylee_beauty_product')


    models = {
        u'hylee_beauty.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hylee_beauty.Category']"}),
            'top': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'hylee_beauty.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'hylee_beauty.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'hylee_beauty.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hylee_beauty.Category']"}),
            'date_available': ('django.db.models.fields.DateField', [], {}),
            'date_import': ('django.db.models.fields.DateTimeField', [], {}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100000'}),
            'dimension_height': ('django.db.models.fields.FloatField', [], {}),
            'dimension_length': ('django.db.models.fields.FloatField', [], {}),
            'dimension_width': ('django.db.models.fields.FloatField', [], {}),
            'ean': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hylee_beauty.Manufacturer']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['hylee_beauty']