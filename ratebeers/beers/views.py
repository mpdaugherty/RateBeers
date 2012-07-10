from django.shortcuts import render_to_response
from models import Beer
from util import json

def get_beer_score(beer):
    return beer.score

def home(req):
    '''
    Displays a list of all the beers in our system in descending order of score.
    '''
    beers = list(Beer.objects.all())
    beers.sort(key=get_beer_score)
    beers.reverse()
    return render_to_response('home.dhtml', { 'beers' : beers })

def like(req, beer_slug):
    '''
    Adds a "like" to a beer.
    '''
    beer = Beer.objects.get(slug=beer_slug)
    beer.num_likes = beer.num_likes + 1
    beer.save()
    return render_to_response('thanks.dhtml', { 'action' : 'liking {}'.format(beer.name) })

def dislike(req, beer_slug):
    '''
    Adds a "dislike" to a beer.
    '''
    beer = Beer.objects.get(slug=beer_slug)
    beer.num_dislikes = beer.num_dislikes + 1
    beer.save()
    return render_to_response('thanks.dhtml', { 'action' : 'disliking {}'.format(beer.name) })

@json
def ajax_like(req, beer_slug):
    '''
    Adds a "like" to a beer and returns JSON.
    '''
    beer = Beer.objects.get(slug=beer_slug)
    beer.num_likes = beer.num_likes + 1
    beer.save()
    return {
        'success' : True,
        'beer' : { 'num_likes': beer.num_likes, 'num_dislikes': beer.num_dislikes, }
        }

@json
def ajax_dislike(req, beer_slug):
    '''
    Adds a "dislike" to a beer and returns JSON.
    '''
    beer = Beer.objects.get(slug=beer_slug)
    beer.num_dislikes = beer.num_dislikes + 1
    beer.save()
    return {
        'success' : True,
        'beer' : { 'num_likes': beer.num_likes, 'num_dislikes': beer.num_dislikes, }
        }

def individual_beer(req, beer_slug):
    '''
    Displays information about a single beer.
    '''
    beer = Beer.objects.get(slug=beer_slug)
    return render_to_response('individual_beer_page.dhtml', { 'beer': beer })
