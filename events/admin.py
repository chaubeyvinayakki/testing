from django.contrib import admin


from .models import Event



class EventModelAdmin(admin.ModelAdmin):

    list_display = ("event_name", "date_time" , "duration", "address", "date_created", "date_modified")#list_display-> will display containing element
    list_display_links = ["date_time"]#list_display_links->will diplay links
    list_editable = ["address"]#address is editable
    list_filter = ["date_time"]#date_time is filterable
    search_fields = ["event_name", "address"]#we can search by event_name and address


    class Meta:
        model=Event#Event is class in model.py
admin.site.register(Event, EventModelAdmin)
