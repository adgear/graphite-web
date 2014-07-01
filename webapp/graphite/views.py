import traceback
from django.conf import settings
from django.http import HttpResponseServerError
from django.template import Context, loader
from graphite.logger import log


def server_error(request, template_name='500.html'):
  template = loader.get_template(template_name)
  stacktrace = traceback.format_exc()
  context = Context({
    'stacktrace' : stacktrace
  })
  msg = "Error handling request: %s: %s" % (request.META['REQUEST_URI'], stacktrace)
  log.exception(msg)
  return HttpResponseServerError( template.render(context) )
