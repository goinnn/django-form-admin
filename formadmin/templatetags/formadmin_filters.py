from django.template.base import Library


from formadmin.forms import as_django_admin as as_django_admin_func

register = Library()


@register.filter
def as_django_admin(form):
    return as_django_admin_func(form)
