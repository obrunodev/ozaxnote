from django.shortcuts import redirect
from config.settings import LOGIN_REDIRECT_URL


def index(request):
    return redirect(LOGIN_REDIRECT_URL)
