from django.contrib import admin
from birds.models import Species, Color, Location, Animal, Event, Status


# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    fields = ('species', 'sex', 'band_color', 'band_number', 'parents')
    list_display = ('name', 'species', 'band', 'uuid', 'sex')
    list_filter = ('species', 'sex', 'band_color')
    search_fields = ('band', 'uuid')
    pass

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'

    fields = ('animal', 'status', 'location', 'description', 'date', 'entered_by')
    list_display = ('animal', 'date', 'status', 'description')
    list_filter = ('animal', 'entered_by', 'status', 'location')
    search_fields = ('animal', 'entered_by', 'description')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Status, StatusAdmin)

for model in (Species, Color, Location):
    admin.site.register(model)
