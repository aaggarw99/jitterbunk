from django.shortcuts import render

from .models import UserProfile, Bunk
from django.utils import timezone
from django.views import generic


def index(request):
    latest_bunks_list = Bunk.objects.order_by('-timestamp')[:5]
	# output = ', '.join([p.question_text for p in latest_question_list])

    context = {
		'latest_bunk_list' : latest_bunk_list, 
	}

	# template = loader.get_template("polls/index.html")
	# return HttpResponse(template.render(context, request))

	# render loads the template in one line
    return render(request, 'jb/index.html', context)

class IndexView(generic.ListView):
	template_name = 'jb/index.html'
	context_object_name = 'latest_bunk_list'

	def get_queryset(self):
		"""Return the last five published questions (not including
		those in the future)."""
		return Bunk.objects.filter(timestamp__lte=timezone.now()).order_by('-timestamp')[:5]