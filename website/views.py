from django.shortcuts import render,redirect
from accounts.platform.hotService import *
from accounts.platform.handlers.sinaHandler import SinaHandler


def content_view(request):
    user = request.user
    if not user.is_authenticated():
        return redirect("index")

    service = StatusService(user)
    ret = service.get_friends_statuses()
    return render(
        request,
        "website/content.html",
        {'user': user, 'timelinecontent': ret.data,'errors':ret.errors},
    )

def statuses_view(request):
    user = request.user
    user.username = 'Eleven'
    sina = SinaHandler(user)
    statuses = sina.statusService.get_friends_statuses(count = 2)
    #if not user.is_authenticated():
    #    return HttpResponseRedirect("index")
    #service = StatusService(user)
    #if service:
    #    content = service.GetFriendsStatuses()
    #else:
    #    content = None
    #content = None
    return render(request, "website/statuses.html", {'user':user,'statuses': statuses})