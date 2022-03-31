# Register your models here.
from django.contrib.admin.models import LogEntry
from django.contrib import admin
from .models import Fanduier, FDReporter,GondanNote,SocietyInsureCardInfo

# Register your models here.

admin.site.site_header = '仁宇劳务公司门户网站后台管理系统-- Python & Django'
admin.site.site_title = '仁宇劳务公司门户网站后台管理系统--Python & Django'
admin.site.index_title = '仁宇劳务管理'
class FanduierAdmin(admin.ModelAdmin):
    list_display = ['id','fadriq','name','bans2','sanj2','bans','sanj']
    list_display.append('colored_name')
   # radio_fields = {'types':admin.HORIZONTAL}
    #readonly_fields = ['bans','sanj','bans2','sanj2']
    ordering = ['-id']
    sortable_by = ['name','fadriq']
    list_display_links = ['id','name']
    list_filter = ['name']
    list_per_page = 40
    list_max_show_all = 100
    #list_editable = ['fadriq']
    search_fields = ['name','fadriq']
   # date_hierarchy = 'created'
    save_as = True
    actions_on_top = False
    actions_on_bottom = True

class FDReporterAdmin(admin.ModelAdmin):
    list_display = ['id','name','yearday','days','sbans2','ssanj2','sbans','ssanj','totals']
    list_display_links = ['id','name','yearday']
    search_fields = ['name','yearday']
    list_filter = ['name']
    list_per_page = 50
    save_as = True
    actions_on_bottom= True


class GondanNoteAdmin(admin.ModelAdmin):
    list_display = ['id','name','cgdate','cgplace','grdescription','begtime','endtime','remark']
    list_display_links = ['id','grdescription']
    search_fields = ['name','cgdate']
    list_filter = ['name']
    list_per_page = 40
    list_max_show_all = 200
    ordering = ['-cgdate']
    
class SocietyInsureCardInfoAdmin(admin.ModelAdmin):
    list_display = ['id','bank','name','card_no','during','account_no','land_address']
    list_display_links = ['id','name','card_no']
    search_fields = ['name','card_no']
    list_filter =['land_address']
    list_per_page = 40
    list_max_show_all = 400
    ordering = ['name']    
#@admin.register(LogEntry,site='127.0.0.1:8009')
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr','object_id','action_flag','user','change_message']
    
    
admin.site.register(Fanduier, FanduierAdmin)
admin.site.register(FDReporter, FDReporterAdmin)
admin.site.register(GondanNote, GondanNoteAdmin)
admin.site.register(SocietyInsureCardInfo,SocietyInsureCardInfoAdmin)
admin.site.register(LogEntry, LogEntryAdmin)