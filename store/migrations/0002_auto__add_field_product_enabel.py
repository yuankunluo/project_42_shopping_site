# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.enabel'
        db.add_column(u'hylee_beauty_product', 'enabel',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.enabel'
        db.delete_column(u'hylee_beauty_product', 'enabel')


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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Category']"}),
            'top': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['store.Category']"}),
            'date_available': ('django.db.models.fields.DateField', [], {}),
            'date_import': ('django.db.models.fields.DateTimeField', [], {}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '100000'}),
            'dimension_height': ('django.db.models.fields.FloatField', [], {}),
            'dimension_length': ('django.db.models.fields.FloatField', [], {}),
            'dimension_width': ('django.db.models.fields.FloatField', [], {}),
            'ean': ('django.db.models.fields.IntegerField', [], {}),
            'enabel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
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
        }
    }

    complete_apps = ['store']