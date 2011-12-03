from django.contrib.admin.helpers import AdminForm
from django.template.loader import render_to_string


def as_django_admin(form):
    fieldsets = getattr(form, 'fieldsets', ())
    prepopulated_fields = getattr(form, 'prepopulated_fields', {})
    readonly_fields = getattr(form, 'readonly_fields', None)
    model_admin = getattr(form, 'model_admin', None)

    if not fieldsets:
        fieldsets = [(None, {'fields': form.fields.keys()})]
    try:
        adminform = AdminForm(form, fieldsets, prepopulated_fields, readonly_fields, model_admin)
    except TypeError:  # To old django
        adminform = AdminForm(form, fieldsets, prepopulated_fields)
    return render_to_string('formadmin/form_admin_django.html', {'adminform': adminform, })


class FormAdminDjango(object):
    """
    Abstract class implemented to provide form django admin like
    Usage::

       class FooForm(forms.Form, FormAdminDjango):
          ...
    """

    fieldsets = ()
    prepopulated_fields = {}
    readonly_fields = None
    model_admin = None

    def as_django_admin(self):
        return as_django_admin(self)
