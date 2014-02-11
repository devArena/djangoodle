# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event.id'
        db.alter_column(u'djangoodle_event', 'id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True))

    def backwards(self, orm):

        # Changing field 'Event.id'
        db.alter_column(u'djangoodle_event', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))

    models = {
        u'djangoodle.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'email_of_creator': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_of_creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 11, 0, 0)'})
        },
        u'djangoodle.eventitem': {
            'Meta': {'object_name': 'EventItem'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangoodle.Event']"}),
            'event_item_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_item_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 11, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'djangoodle.participant': {
            'Meta': {'object_name': 'Participant'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangoodle.Event']"}),
            'event_items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['djangoodle.EventItem']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_of_authorization': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 11, 0, 0)'})
        }
    }

    complete_apps = ['djangoodle']