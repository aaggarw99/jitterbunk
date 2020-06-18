from django.shortcuts import render

from .models import UserProfile, Bunk
from django.utils import timezone
from django.views import generic


def index(request):
    latest_bunks_list = Bunk.objects.order_by('-timestamp')[:5]
	# output = ', '.join([p.question_text for p in latest_question_list])
    all_user_profiles = UserProfile.objects.order_by('-user')

    context = {
		'latest_bunk_list' : latest_bunk_list,
        'all_user_profiles' : all_user_profiles,
	}

	# template = loader.get_template("polls/index.html")
	# return HttpResponse(template.render(context, request))

	# render loads the template in one line
    return render(request, 'jb/index.html', context)

class IndexView(generic.ListView):
    template_name = 'jb/index.html'
    context_object_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_user_profiles'] = UserProfile.objects.order_by('-user')
        context['latest_bunk_list'] = Bunk.objects.order_by('-timestamp')[:5]
        return context
        
    def get_queryset(self):
        """Return the last five published questions (not including
        those in the future)."""
        return Bunk.objects.filter(timestamp__lte=timezone.now()).order_by('-timestamp')[:5]

def detail(request, bunk_id):
    bunk = get_object_or_404(Bunk, pk=bunk_id)
    return render(request, "jb/detail.html", {'bunk': bunk})

class DetailView(generic.DetailView):
    model = Bunk
    template_name = 'jb/detail.html'

    # def get_queryset(self):
    #     return Bunk.objects.filter(timestamp__lte=timezone.now())

def userprofile(request, up_id):
    up = get_object_or_404(UserProfile, pk=up_id)
    return render(request, "jb/userprofile.html", {"up" : up})

class UserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'jb/userprofile.html'

    def get_queryset(self):
        return UserProfile.objects.all()