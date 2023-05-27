from django.http import JsonResponse, HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import telebot
import json
from .models import Session, History
from .gpt import call_chat

TOKEN = '6063794957:AAFRLqmybg9fnCde4OqQuP-7QdKSqnQ13HY'
tbot = telebot.TeleBot(TOKEN)


@csrf_exempt
def bot(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = json.loads(request.body)
        chat_id = json_data["message"]["chat"]["id"]
        print(chat_id)
        session = Session.objects.get_or_create(external_id=chat_id, defaults={"ad_id": 1})[0]
        History.objects.create(session=session, text={"role": "user", "content": json_data["message"]["text"]})
        chat_response = call_chat(session)
        tbot.send_message(chat_id, chat_response)
        return JsonResponse({"success": True})
    else:
        raise PermissionDenied


@tbot.message_handler(commands=['start'])
def greet(m):
    tbot.send_message(m.chat.id, "Hello")
