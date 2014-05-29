# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Todo.due_date'
        db.add_column(u'todos_todo', 'due_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Todo.is_done'
        db.add_column(u'todos_todo', 'is_done',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field assigned_to on 'Todo'
        m2m_table_name = db.shorten_name(u'todos_todo_assigned_to')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('todo', models.ForeignKey(orm[u'todos.todo'], null=False)),
            ('user', models.ForeignKey(orm[u'custom_auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['todo_id', 'user_id'])

        # Deleting field 'TodoList.name'
        db.delete_column(u'todos_todolist', 'name')

        # Adding field 'TodoList.title'
        db.add_column(u'todos_todolist', 'title',
                      self.gf('django.db.models.fields.CharField')(default='No Title', max_length=50),
                      keep_default=False)

        # Adding field 'TodoList.parent'
        db.add_column(u'todos_todolist', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['todos.TodoList']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Todo.due_date'
        db.delete_column(u'todos_todo', 'due_date')

        # Deleting field 'Todo.is_done'
        db.delete_column(u'todos_todo', 'is_done')

        # Removing M2M table for field assigned_to on 'Todo'
        db.delete_table(db.shorten_name(u'todos_todo_assigned_to'))


        # User chose to not deal with backwards NULL issues for 'TodoList.name'
        raise RuntimeError("Cannot reverse this migration. 'TodoList.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'TodoList.name'
        db.add_column(u'todos_todolist', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=50),
                      keep_default=False)

        # Deleting field 'TodoList.title'
        db.delete_column(u'todos_todolist', 'title')

        # Deleting field 'TodoList.parent'
        db.delete_column(u'todos_todolist', 'parent_id')


    models = {
        u'custom_auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'todos.todo': {
            'Meta': {'ordering': "('modified_on', 'created_on')", 'object_name': 'Todo'},
            'assigned_to': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'todos'", 'symmetrical': 'False', 'to': u"orm['custom_auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_done': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'todos'", 'to': u"orm['todos.TodoList']"}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'todos.todolist': {
            'Meta': {'ordering': "('title',)", 'object_name': 'TodoList'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': u"orm['todos.TodoList']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['todos']