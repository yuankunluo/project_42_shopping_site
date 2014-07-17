# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.created_at'
        db.add_column(u'account_order', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Order.order_id'
        db.add_column(u'account_order', 'order_id',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 7, 17, 0, 0), max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.created_at'
        db.delete_column(u'account_order', 'created_at')

        # Deleting field 'Order.order_id'
        db.delete_column(u'account_order', 'order_id')


    models = {
        u'account.order': {
            'Meta': {'ordering': "['created_at']", 'object_name': 'Order'},
            'cart_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'shipping_add': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_to': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_zip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['account']