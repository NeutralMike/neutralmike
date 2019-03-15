from django.shortcuts import render, redirect
import vk
from urllib import request as urlrequest
import json

client_id = "6896687"
redirect_uri = "http://neutralmike.ru/webim-test/"
version = "5.92"
client_secret = "07T9inWRpysoiRDcxePI"


def test(request):
    friends = None
    self = None
    code = None
    try:
        if request.session["auth"] is False:
            code = request.GET['code']
            content = json.loads(vk_access(code))
            access_token = content["access_token"]
            request.session["access_token"] = access_token
            request.session["auth"] = True
            request.session.set_expiry(3600)
            return redirect("http://neutralmike.ru/webim-test/")
        session = vk.Session(access_token=request.session["access_token"])
        api = vk.API(session, v=version)
        try:
            friends = api.friends.get(fields="name,domain", count=5)["items"]
            self = api.users.get(fields="name,domain")[0]
        except Exception as e:
            pass
    except Exception as e:
        request.session["auth"] = False
    return render(request, 'index.html', {"auth": request.session["auth"], "self": self, "friends": friends})


def vk_auth(request):
    return redirect("https://oauth.vk.com/authorize?"+"client_id="+client_id+
                    "&redirect_uri="+redirect_uri+"&v="+version+"&scope=friends")


def vk_access(code):
    return urlrequest.urlopen("https://oauth.vk.com/access_token?"+"client_id="+client_id+"&client_secret="+client_secret+
                    "&redirect_uri="+redirect_uri+"&code="+code).read().decode('utf-8')
