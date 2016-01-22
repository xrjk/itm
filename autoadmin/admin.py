#_*_coding:utf-8_*_
from django.contrib import admin
import models

class ServerAppCategAdmin(admin.ModelAdmin):
    list_display = ('id', 'server_categ_id', 'app_categ_name')

class ServerFunCategAdmin(admin.ModelAdmin):
    list_display = ('id', 'server_categ_name')

class ServerListAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'server_wip', 'server_lip', 'server_op', 'server_app_id')

class ModuleListAdmin(admin.ModelAdmin):
    list_display = ('id', 'module_name', 'module_caption', 'module_extend')


admin.site.register(models.ServerAppCateg,ServerAppCategAdmin)
admin.site.register(models.ServerFunCateg,ServerFunCategAdmin)
admin.site.register(models.ServerList,ServerListAdmin)
admin.site.register(models.ModuleList,ModuleListAdmin)
