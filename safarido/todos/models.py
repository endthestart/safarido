from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(_('created on'), auto_now_add=True)
    modified_on = models.DateTimeField(_('modified on'), auto_now=True)

    class Meta:
        abstract = True


class TodoList(TimestampedModel):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ('name', )


class Todo(TimestampedModel):
    list = models.ForeignKey(TodoList)
    title = models.CharField(_('title'), max_length=200)
    description = models.TextField(_('description'))

    class Meta:
        ordering = ('modified_on', 'created_on', )
