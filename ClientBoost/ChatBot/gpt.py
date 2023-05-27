import openai
from .models import Session, History


def call_chat(session: Session) -> str:
    base_contexts = list(session.ad.contexts.all().values_list("data", flat=True))
    history_contexts = list(session.histories.all().values_list("text", flat=True))
    print(base_contexts, history_contexts)
    contexts = base_contexts + history_contexts
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=contexts
    )
    response_text = {"role": response["choices"][0]["message"]["role"],
                     "content": response["choices"][0]["message"]["content"]}
    History.objects.create(session=session, text=response_text)
    return response_text["content"]