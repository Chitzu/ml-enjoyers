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
        message_text = json_data["message"]["text"]
        print(message_text)
        if message_text.startswith('/start'):
            command, _, param = message_text.partition(' ')
            session = Session.objects.create(external_id=chat_id, ad_id=param)
            tbot.send_message(chat_id, session.ad.first_text)
        else:
            try:
                session = Session.objects.get(external_id=chat_id)
                History.objects.create(session=session, text={"role": "user", "content": message_text})
                chat_response = call_chat(session)
                tbot.send_message(chat_id, chat_response)
            except Exception as e:
                print(e)
        return JsonResponse({"success": True})
    else:
        raise PermissionDenied


def view_ad(request):
    from django.shortcuts import render
    return render(request, 'ChatBot/ad_1.html')
    pass

