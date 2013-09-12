from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import FormView

from .forms import SendEmailForm


class SendEmailView(FormView):

    form_class = SendEmailForm

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(SendEmailView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        raise NotImplementedError

    def get_context_data(self, *args, **kwargs):
        context = super(SendEmailView, self).get_context_data(*args, **kwargs)
        extra_context = {'title': _('Send email')}
        extra_context.update(context)
        return extra_context
