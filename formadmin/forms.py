from django.contrib.admin.helpers import AdminForm
from django.template.loader import render_to_string


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
        if not self.fieldsets:
            self.fieldsets = [(None, {'fields': self.fields.keys()})]
        adminform = AdminForm(self, self.fieldsets, self.prepopulated_fields, self.readonly_fields, self.model_admin)
        return render_to_string('formadmin/form_admin_django.html', {'adminform': adminform, })
