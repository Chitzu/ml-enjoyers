from django.http import JsonResponse, HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import telebot
import json

TOKEN = '6063794957:AAFRLqmybg9fnCde4OqQuP-7QdKSqnQ13HY'
tbot = telebot.TeleBot(TOKEN)


@csrf_exempt
def bot(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = json.loads(request.body)
        tbot.send_message(json_data["message"]["chat"]["id"], "asdsad")
        return JsonResponse({"success": True})
    else:
        raise PermissionDenied


@tbot.message_handler(commands=['start'])
def greet(m):
    tbot.send_message(m.chat.id, "Hello")
