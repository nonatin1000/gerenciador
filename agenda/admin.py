# -*- encoding: utf-8 -*-

from agenda.models import ItemAgenda
from django.contrib import admin

class ItemAgendaAdmin(admin.ModelAdmin):
	fields = ('titulo', 'data', 'hora', 'descricao', 'participantes')
	list_display = ('data', 'hora', 'titulo', 'usuario')
	list_display_links = ('data', 'hora', 'titulo')
	list_filter = ('usuario',)

	def queryset(self, request):
		qs = super(ItemAgendaAdmin, self).queryset(request)
		if request.user.is_superuser:
			return qs
		
		return qs.filter(usuario = request.user)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

admin.site.register(ItemAgenda, ItemAgendaAdmin)



