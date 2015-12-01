from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from models import Movie
from django.shortcuts import render_to_response
from django.template import RequestContext
import json as simplejson
from django.db import connection

"""
Returns Index page 
"""
def index(request):
  return render_to_response('index.html',context_instance=RequestContext(request))

"""
Gives static data for a movie in JSON format
"""
def getStaticData(request):
  cursor = connection.cursor()
  cursor.execute('''Select id,name,popularity,indb_score,director from imdb_movie''')
  data=cursor.fetchall()
  result = {}
  for row in data:
      movieData = {}
      movieData['name'] = row[1]
      movieData['popularity'] = float(row[2])
      movieData['imdb_score'] = float(row[3])
      movieData['director'] = row[4]
      result[row[0]] = movieData
    
  returnData=simplejson.dumps(result)
  return HttpResponse(returnData,content_type="application/json")
