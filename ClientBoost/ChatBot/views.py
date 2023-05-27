from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@csrf_exempt
@require_POST
def webhook_view(request):
    # In a real use case, you'd do something with the data you've received.
    # This could be anything from storing it in your database, sending an email,
    # updating other systems, etc.
    # You should also check the validity and authenticity of the received data.

    # Parse the JSON data from the request body
    data = json.loads(request.body)

    # Do something with the data...

    # Return a response to acknowledge receipt of the data
    return HttpResponse(status=200)