.. contents::

=================
django-form-admin
=================

Information
===========

It is a Django application that lets to render forms like django admin, with the same HTML


How to use it
=============

In your form:

::

    class FooForm(forms.Form, FormAdminDjango):
        pass

    class FooModelForm(forms.ModelForm, FormAdminDjango):
        pass

In your template:

::

    {{ form.as_django_admin }}

But you don't need inherit of FormAdminDjango, you may also do

::

    class FooForm(forms.Form):
        ...

        def as_django_admin(self):
            from formadmin.forms import as_django_admin
            return as_django_admin(self)


Development
===========

You can get the bleeding edge version of django-form-admin by doing a clone
of its git repository::

  git clone git://github.com/Yaco-Sistemas/django-form-admin.git
