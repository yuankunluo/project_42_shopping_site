# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Manufacturer'
        db.create_table(u'store_manufacturer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'store', ['Manufacturer'])

        # Adding model 'Category'
        db.create_table(u'store_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Category'])),
        ))
        db.send_create_signal(u'store', ['Category'])

        # Adding model 'Brand'
        db.create_table(u'store_brand', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=10000)),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Manufacturer'])),
        ))
        db.send_create_signal(u'store', ['Brand'])

        # Adding model 'Image'
        db.create_table(u'store_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'store', ['Image'])

        # Adding model 'Product'
        db.create_table(u'store_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=100000)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('ean', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('date_available', self.gf('django.db.models.fields.DateField')()),
            ('date_import', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')()),
            ('dimension_length', self.gf('django.db.models.fields.FloatField')()),
            ('dimension_height', self.gf('django.db.models.fields.FloatField')()),
            ('dimension_width', self.gf('django.db.models.fields.FloatField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
            ('manufacturer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Manufacturer'])),
            ('brand', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Brand'])),
            ('onsale', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sale_price', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('sale_date_start', self.gf('django.db.models.fields.DateField')()),
            ('sale_date_end', self.gf('django.db.models.fields.DateField')()),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'store', ['Product'])

        # Adding model 'ProductHasCategories'
        db.create_table(u'store_producthascategories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Product'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['store.Category'])),
        ))
        db.send_create_signal(u'store', ['ProductHasCategories'])


    def backwards(self, orm):
        # Deleting model 'Manufacturer'
        db.delete_table(u'store_manufacturer')

        # Deleting model 'Category'
        db.delete_table(u'store_category')

        # Deleting model 'Brand'
        db.delete_table(u'store_brand')

        # Deleting model 'Image'
        db.delete_table(u'store_image')

        # Deleting model 'Product'
        db.delete_table(u'store_product')

        # Deleting model 'ProductHasCategories'
        db.delete_table(u'store_producthascategories')


    models = {
        u'store.brand': {
            'Meta': {'object_name': 'Brand'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Manufacturer']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'store.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Category']"})
        },
        u'store.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'store.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'store.product': {
            'Meta': {'object_name': 'Product'},
            'brand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Brand']"}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['store.Category']", 'through': u"orm['store.ProductHasCategories']", 'symmetrical': 'False'}),
            'date_available': ('django.db.models.fields.DateField', [], {}),
            'date_import': ('django.db.models.fields.DateTimeField', [], {}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100000'}),
            'dimension_height': ('django.db.models.fields.FloatField', [], {}),
            'dimension_length': ('django.db.models.fields.FloatField', [], {}),
            'dimension_width': ('django.db.models.fields.FloatField', [], {}),
            'ean': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Manufacturer']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'onsale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sale_date_end': ('django.db.models.fields.DateField', [], {}),
            'sale_date_start': ('django.db.models.fields.DateField', [], {}),
            'sale_price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'store.producthascategories': {
            'Meta': {'object_name': 'ProductHasCategories'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Product']"})
        }
    }

    complete_apps = ['store']