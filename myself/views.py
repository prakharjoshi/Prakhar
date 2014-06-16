from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse


def home(request):
	return render_to_response('myself/frontpage.html',context_instance=RequestContext(request))


