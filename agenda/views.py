# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404
from models import ItemAgenda
from forms import FormItemAgenda
from django.template import RequestContext

def lista(request):
	lista_itens = ItemAgenda.objects.all()
	return render_to_response("lista.html", {'lista_itens': lista_itens}, context_instance=RequestContext(request))

def adiciona(request):
	if request.method == "POST":
		form = FormItemAgenda(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response("salvo.html", {})
	else:
		form = FormItemAgenda()
	form = FormItemAgenda()
	return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))


def item(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item)
	if request.method == "POST":
		form = FormItemAgenda(request.POST, request.FILES, instance=item)
		if form.is_valid():
			form.save()
			return render_to_response("atualizado.html", {})
	else:
		form = FormItemAgenda(instance=item)
	return render_to_response("item.html", {'form': form}, context_instance=RequestContext(request))

def remove(request, nr_item):
	item = get_object_or_404(ItemAgenda, pk=nr_item)
	if request.method == 'POST':
		item.delete()
		return render_to_response("removido.html", {})
	return render_to_response("remove.html", {'item': item}, context_instance=RequestContext(request))
