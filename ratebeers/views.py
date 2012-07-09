from django.http import HttpResponse
from django.shortcuts import render_to_response

from random_quote import quotes, get_quote

def home(req):
    return HttpResponse(get_quote())

def home_with_template(req):
    context = {
        'quote': get_quote(),
    }
    return render_to_response('home.django', context)

def specific_quote(req, quote_index):
    quote_index = int(quote_index)

    try:
        quote = quotes[quote_index]
    except IndexError:
        quote = 'This quote does not exist'
    return render_to_response('home.django', { 'quote': quote })
