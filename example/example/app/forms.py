from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SendEmailForm(forms.Form):
    subject = forms.CharField(label=_('Subject'))
    body = forms.CharField(widget=forms.Textarea, label=_('Body'))
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(),
                                           label=_('Users'),
                                           widget=admin_widgets.FilteredSelectMultiple(_('Users'), False))
    date_send = forms.SplitDateTimeField(label=_('Date send'),
                                         widget=admin_widgets.AdminSplitDateTime)

    fieldsets = (
        (None, {
            'fields': ('subject', 'body',)
        }),
        ('Options', {
            'fields': ('date_send', 'users')
        }),
    )
