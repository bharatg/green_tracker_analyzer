from django.shortcuts import render

from django.http import HttpResponse
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, redirect
from simpletable.models import SimpleTable

from localconnect import connect

list_of_users = connect()
print(list_of_users)
def index(request):
  queue = SimpleTable.objects.order_by("id")
  c = {'queue': queue}
  #print(c['queue'])
  #c = {}
  for row in list_of_users:
      c[row[0]] = SimpleTable(usr_id =  row[0], name=row[1])
  c.update(csrf(request))
  return render_to_response('index.html', c)

#def add(request):
#  item = SimpleTable(text=request.POST["text"])
#  item.save()
#  return HttpResponse("<li>%s</li>" % item.text)

#def remove(request):
#  items = SimpleTable.objects.order_by("id")[:1]
#  if len(items) != 0:
#    items[0].delete()
#  return redirect("/")
