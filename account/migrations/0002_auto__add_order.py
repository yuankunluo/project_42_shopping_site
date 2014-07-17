# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'account_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cart_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('total_price', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=9, decimal_places=2)),
            ('shipping_to', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_add', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shipping_zip', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'account', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'account_order')


    models = {
        u'account.order': {
            'Meta': {'object_name': 'Order'},
            'cart_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shipping_add': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_to': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'shipping_zip': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['account']