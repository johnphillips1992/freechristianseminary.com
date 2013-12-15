# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Degree'
        db.create_table('seminary_degree', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('certificate', self.gf('django.db.models.fields.files.FileField')(null=True, max_length=100, blank=True)),
        ))
        db.send_create_signal('seminary', ['Degree'])

        # Adding model 'Course'
        db.create_table('seminary_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('degree', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seminary.Degree'], related_name='courses')),
            ('certificate', self.gf('django.db.models.fields.files.FileField')(null=True, max_length=100, blank=True)),
        ))
        db.send_create_signal('seminary', ['Course'])

        # Adding model 'Section'
        db.create_table('seminary_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, max_length=255, blank=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seminary.Course'], related_name='sections')),
            ('content', self.gf('djangocms_text_ckeditor.fields.HTMLField')(null=True, blank=True)),
        ))
        db.send_create_signal('seminary', ['Section'])

        # Adding model 'Question'
        db.create_table('seminary_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seminary.Course'], related_name='questions')),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('answer_a', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('answer_b', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('answer_c', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('answer_d', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('correct_answer', self.gf('django.db.models.fields.CharField')(null=True, max_length=1, blank=True)),
        ))
        db.send_create_signal('seminary', ['Question'])

        # Adding model 'Score'
        db.create_table('seminary_score', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='+')),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['seminary.Course'], related_name='scores')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('score', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('seminary', ['Score'])


    def backwards(self, orm):
        # Deleting model 'Degree'
        db.delete_table('seminary_degree')

        # Deleting model 'Course'
        db.delete_table('seminary_course')

        # Deleting model 'Section'
        db.delete_table('seminary_section')

        # Deleting model 'Question'
        db.delete_table('seminary_question')

        # Deleting model 'Score'
        db.delete_table('seminary_score')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seminary.course': {
            'Meta': {'object_name': 'Course'},
            'certificate': ('django.db.models.fields.files.FileField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'degree': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seminary.Degree']", 'related_name': "'courses'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'seminary.degree': {
            'Meta': {'object_name': 'Degree'},
            'certificate': ('django.db.models.fields.files.FileField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'seminary.question': {
            'Meta': {'object_name': 'Question'},
            'answer_a': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'answer_b': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'answer_c': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'answer_d': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'correct_answer': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seminary.Course']", 'related_name': "'questions'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
        },
        'seminary.score': {
            'Meta': {'object_name': 'Score'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seminary.Course']", 'related_name': "'scores'"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'+'"})
        },
        'seminary.section': {
            'Meta': {'object_name': 'Section'},
            'content': ('djangocms_text_ckeditor.fields.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['seminary.Course']", 'related_name': "'sections'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['seminary']