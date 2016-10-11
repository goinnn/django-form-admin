.. contents::

=================
django-form-admin
=================

Information
===========

.. image:: https://badge.fury.io/py/django-form-admin.png
    :target: https://badge.fury.io/py/django-form-admin

.. image:: https://pypip.in/d/django-form-admin/badge.png
    :target: https://pypi.python.org/pypi/django-form-admin

It is a Django application that lets to render forms like django admin, with the same HTML


Requirements
============

 * `Django <https://www.djangoproject.com/>`_ (>= 1.0, the `example project <https://github.com/Yaco-Sistemas/django-form-admin/tree/master/example>`_ needs >=1.3)

How to use it
=============

Option 1
--------

In your form:

.. code-block:: python

    class FooForm(forms.Form, FormAdminDjango):
        pass

    class FooModelForm(forms.ModelForm, FormAdminDjango):
        pass

In your template:

.. code-block:: html+django

    {{ form.as_django_admin }}

Option 2
--------

But you don't need inherit of FormAdminDjango, you may also do

In your form:

.. code-block:: python

    class FooForm(forms.Form):
        ...

        def as_django_admin(self):
            from formadmin.forms import as_django_admin
            return as_django_admin(self)


In your template:

.. code-block:: html+django

    {{ form.as_django_admin }}


Option 3
--------

Or even without modify the form

Only in your template:

.. code-block:: html+django

    {% load formadmin_filters %}
    {{ form|as_django_admin }}


Development
===========

You can get the bleeding edge version of django-form-admin by doing a clone
of its git repository::

  git clone git://github.com/Yaco-Sistemas/django-form-admin.git
