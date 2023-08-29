from django.contrib import admin
from .models import currency
from .models import member_acc


# admin.site.register(currency)
# admin.site.register(member_acc)


class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "Date",)
  
admin.site.register(member_acc, MemberAdmin)



class MemberAdmin(admin.ModelAdmin):
  list_display = ("Currencyone", "Currencytwo", "Valueone", "Valuetwo")
  
admin.site.register(currency, MemberAdmin)