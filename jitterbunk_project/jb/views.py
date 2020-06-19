from django.shortcuts import render, get_object_or_404

from .models import UserProfile, Bunk
from django.utils import timezone
from django.views import generic
from django.contrib.auth.decorators import login_required


def index(request):
    """
    Loads the index page that lists both the most recent bunks
    and all users in the system.
    """
    latest_bunk_list = Bunk.objects.order_by('-timestamp')[:10]
    all_user_profiles = UserProfile.objects.order_by('-user')

    context = {
        'latest_bunk_list' : latest_bunk_list,
        'all_user_profiles' : all_user_profiles,
    }

    # render loads the template in one line
    return render(request, 'jb/index.html', context)

def bunk_detail(request, bunk_id):
    """
    Loads the bunk detail page that gives more information about
    a certain bunk.
    """
    bunk = get_object_or_404(Bunk, pk=bunk_id)
    return render(request, "jb/bunk_detail.html", {'bunk': bunk})

def user_profile(request, up_id):
    """
    Loads a user's profile page.
    """
    up = get_object_or_404(UserProfile, pk=up_id)
    return render(request, "jb/user_profile.html", {"userprofile" : up})

@login_required
def bunk(request, user1_id, user2_id):
    """
    Performs bunk action where USER1_ID bunks USER2_ID.
    """
    user1 = get_object_or_404(UserProfile, pk=user1_id)
    user2 = get_object_or_404(UserProfile, pk=user2_id)

    new_bunk = Bunk(from_user=user1, to_user=user2, timestamp=timezone.now())
    new_bunk.save()

    return render(request, "jb/bunk_success.html", {"userprofile1":user1, "userprofile2":user2})

@login_required
def user_feed(request, user_id):
    """
    Displays the signed in user's own bunk feed.
    """
    print(type(user_id))
    user_id = int(user_id)
    bunk_id_list = [b.id for b in Bunk.objects.all() if b.from_user.id == user_id or b.to_user.id == user_id]
    bunk_list = [get_object_or_404(Bunk, pk=bid) for bid in bunk_id_list]

    return render(request, "jb/user_feed.html", {"bunk_list" : bunk_list})

def bunk_statistics(request):
    """
    Displays all bunk statistics supported.
    """
    userprofiles = UserProfile.objects.all()

    num_bunks_sent = {up:0 for up in userprofiles}
    num_bunks_received = {up:0 for up in userprofiles}

    for bunk in Bunk.objects.all():
        num_bunks_sent[bunk.from_user] += 1
        num_bunks_received[bunk.to_user] += 1

    statistics = [
        Statistic("Number of Bunks Sent", "Shows the number of bunks each user has sent.", num_bunks_sent),
        Statistic("Number of Bunks Received", "Shows the number of bunks each user has received.", num_bunks_received)
    ]

    return render(request, "jb/statistics.html", {"statistics" : statistics, "userprofiles" : userprofiles})



class Statistic:
    
    def __init__(self, name, description, user_value):
        self.name = name
        self.description = description
        self.user_value = user_value