# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'djangoodle_event', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('time_of_creation', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 8, 0, 0))),
            ('email_of_creator', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
        ))
        db.send_create_signal(u'djangoodle', ['Event'])

        # Adding model 'EventItem'
        db.create_table(u'djangoodle_eventitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djangoodle.Event'])),
            ('event_item_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 8, 0, 0))),
            ('event_item_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'djangoodle', ['EventItem'])

        # Adding model 'Participant'
        db.create_table(u'djangoodle_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djangoodle.Event'])),
            ('time_of_authorization', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 4, 8, 0, 0))),
        ))
        db.send_create_signal(u'djangoodle', ['Participant'])

        # Adding M2M table for field event_items on 'Participant'
        m2m_table_name = db.shorten_name(u'djangoodle_participant_event_items')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participant', models.ForeignKey(orm[u'djangoodle.participant'], null=False)),
            ('eventitem', models.ForeignKey(orm[u'djangoodle.eventitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['participant_id', 'eventitem_id'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'djangoodle_event')

        # Deleting model 'EventItem'
        db.delete_table(u'djangoodle_eventitem')

        # Deleting model 'Participant'
        db.delete_table(u'djangoodle_participant')

        # Removing M2M table for field event_items on 'Participant'
        db.delete_table(db.shorten_name(u'djangoodle_participant_event_items'))


    models = {
        u'djangoodle.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'email_of_creator': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_of_creation': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 8, 0, 0)'})
        },
        u'djangoodle.eventitem': {
            'Meta': {'object_name': 'EventItem'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangoodle.Event']"}),
            'event_item_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_item_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 8, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'djangoodle.participant': {
            'Meta': {'object_name': 'Participant'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['djangoodle.Event']"}),
            'event_items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['djangoodle.EventItem']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_of_authorization': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 8, 0, 0)'})
        }
    }

    complete_apps = ['djangoodle']