from django.contrib import admin
from .models import Bid, Blog, Tuning


class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'color', 'size', 'quantity','time_created')
    list_filter = ('time_created',)


admin.site.register(Bid, BidAdmin)
admin.site.register(Blog)
admin.site.register(Tuning)
