from django.contrib import admin

from bands.models import Musician, Band

# This is the minimum line to add your model
# admin.site.register(Musician)

# This is an enhanced way of adding models to admin
# This one allows for customization
@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "birth", "show_weekday")  # the 'show_weekday' is a callable -- not a field
    search_fields = ("last_name__startswith", "first_name__startswith", )
    list_filter = ("birth",) 
    
    
    def show_weekday(self, obj):
        # Fetch weekday of artist’s birth
        return obj.birth.strftime("%A")

    show_weekday.short_description = "Birth Weekday" # column header

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass