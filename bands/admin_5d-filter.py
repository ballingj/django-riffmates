from django.contrib import admin

from bands.models import Musician, Band
from datetime import datetime, date

# This is the minimum line to add a model
# admin.site.register(Musician)

# This is an enhanced way of adding models to admin
# This one allows for customization
# @admin.register(Musician)
# class MusicianAdminOld(admin.ModelAdmin):
#     list_display = ("id", "last_name", "birth", "show_weekday")  # the 'show_weekday' is a callable -- not a field
#     search_fields = ("last_name__startswith", "first_name__startswith", )
#     list_filter = ("birth",) 
    
    
#     def show_weekday(self, obj):
#         # Fetch weekday of artist’s birth
#         return obj.birth.strftime("%A") # format %A is for the weekday

#     show_weekday.short_description = "Birth Weekday" # custom column header

# This is a custom filter
class DecadeListFilter(admin.SimpleListFilter):
    title = 'decade born'
    parameter_name = 'decade'
    
    def lookups(self, request, model_admin):
        result = []
        
        this_year = datetime.today().year
        this_decade = (this_year // 10) * 10
        start = this_decade - 10
        for year in range(start, start - 100, -10):
            result.append( (str(year), f"{year}-{year+9}") )
        return result
            
    def queryset(self, request, queryset):
        start = self.value()
        if start is None:
            return queryset
        
        start = int(start)
        result = queryset.filter(
            birth__gte=date(start, 1, 1),
            birth__lte=date(start + 9, 12, 31),
        )
        return result

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "birth", "show_weekday")  # the 'show_weekday' is a callable -- not a field
    search_fields = ("last_name__startswith", "first_name__startswith", )
    # list_filter = ("birth", ) 
    list_filter = (DecadeListFilter, ) 
    
    
    def show_weekday(self, obj):
        # Fetch weekday of artist’s birth
        return obj.birth.strftime("%A") # format %A is for the weekday

    show_weekday.short_description = "Birth Weekday" # custom column header

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass    # for now inherited ModelAdmin provides all the basic page

