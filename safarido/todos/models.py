from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(_('created on'), auto_now_add=True)
    modified_on = models.DateTimeField(_('modified on'), auto_now=True)

    class Meta:
        abstract = True


class TodoList(TimestampedModel):
    title = models.CharField(
        _('title'),
        max_length=50,
    )
    slug = models.SlugField()
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
    )

    def get_ancestors(self):
        ancestors = []
        if self.parent:
            parent = self.parent
            while parent:
                ancestors.append(parent)
                parent = parent.parent
        ancestors.reverse()
        ancestors = ancestors + [self, ]
        return ancestors

    def save(self, **kwargs):
        # Generate a slug if there is not one
        if self.title and not self.slug:
            self.slug = slugify(self.title)

        super(TodoList, self).save(**kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title', )
        permissions = (
            ('is_owner', 'Is Owner'),
            ('view_todo_list', 'View Todo List'),
        )


class Todo(TimestampedModel):
    list = models.ForeignKey(
        TodoList,
        related_name='todos',
    )
    title = models.CharField(
        _('title'),
        max_length=200)
    description = models.TextField(
        _('description'),
    )
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('users'),
        related_name='todos',
    )
    due_date = models.DateField(
        verbose_name=_('due date'),
        blank=True,
        null=True,
    )
    is_done = models.DateField(
        verbose_name=_('is done'),
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ('modified_on', 'created_on', )
