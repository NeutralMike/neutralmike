from django.shortcuts import render, redirect
import vk
from urllib import request as urlrequest
import json
from django.conf import settings


def index(request):
    friends = None
    self = None
    redirect_uri = f'{request.scheme}://{request.get_host()}/webim-test/'
    try:
        if request.session["auth"] is False:
            code = request.GET['code']
            content = json.loads(vk_access(code, redirect_uri))
            access_token = content["access_token"]
            request.session["access_token"] = access_token
            request.session["auth"] = True
            request.session.set_expiry(3600)
            return redirect("http://neutralmike.ru/webim-test/")
        session = vk.Session(access_token=request.session["access_token"])
        api = vk.API(session, v=settings.VK_VERSION)
        try:
            friends = api.friends.get(fields="name,domain", count=5)["items"]
            self = api.users.get(fields="name,domain")[0]
        except Exception as e:
            pass
    except Exception as e:
        request.session["auth"] = False
    return render(request, 'webim-test.html', {"auth": request.session["auth"], "self": self, "friends": friends})


def vk_auth(request):
    redirect_uri = f'{request.scheme}://{request.get_host()}/webim-test/'
    return redirect("https://oauth.vk.com/authorize?"+"client_id="+settings.CLIENT_ID+
                    "&redirect_uri="+redirect_uri+"&v="+settings.VK_VERSION+"&scope=friends")


def vk_access(code, redirect_uri):
    return urlrequest.urlopen("https://oauth.vk.com/access_token?"+"client_id="+settings.CLIENT_ID+"&client_secret="+settings.CLIENT_SECRET+
                    "&redirect_uri="+redirect_uri+"&code="+code).read().decode('utf-8')
