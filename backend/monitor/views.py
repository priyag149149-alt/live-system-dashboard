from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Users, Sessions

import json
import psutil

from datetime import datetime


@csrf_exempt
def login_view(request):

    try:

        if request.method == "POST":

            data = json.loads(request.body)

            username = data.get("username")
            password = data.get("password")

            print(username)
            print(password)

            user = Users.objects.filter(
                username=username,
                password=password
            ).first()

            if user:

                request.session['user_id'] = user.id

                Sessions.objects.create(
                    user=user,
                    active=True
                )

                return JsonResponse({
                    "message": "Login Success"
                })

            else:

                return JsonResponse({
                    "message": "Invalid Credentials"
                }, status=401)

        return JsonResponse({
            "message": "Only POST allowed"
        })

    except Exception as e:

        print(e)

        return JsonResponse({
            "message": str(e)
        }, status=500)


@csrf_exempt
def logout_view(request):

    request.session.flush()

    return JsonResponse({
        "message": "Logged Out"
    })


def me_view(request):

    user_id = request.session.get('user_id')

    if not user_id:

        return JsonResponse({
            "message": "Not logged in"
        }, status=401)

    user = Users.objects.get(id=user_id)

    return JsonResponse({
        "username": user.username
    })


def stats_view(request):

    try:

        cpu = psutil.cpu_percent()

        memory = psutil.virtual_memory().percent

        active_users = Sessions.objects.filter(
            active=True
        ).count()

        server_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        return JsonResponse({
            "cpu": cpu,
            "memory": memory,
            "active_users": active_users,
            "server_time": server_time
        })

    except Exception as e:

        print(e)

        return JsonResponse({
            "error": str(e)
        })