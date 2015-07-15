# -*- encoding: utf-8 -*-

from agenda.models import ItemAgenda
from django.contrib import admin

class ItemAgendaAdmin(admin.ModelAdmin):
	list_filter = ('usuario',)
	fields = ('titulo', 'data', 'hora', 'descricao')
	list_display = ('data', 'hora', 'titulo')

	def queryset(self, request):
		qs = super(ItemAgendaAdmin, self).queryset(request)
		return qs.filter(usuario=request.user)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

admin.site.register(ItemAgenda, ItemAgendaAdmin)



