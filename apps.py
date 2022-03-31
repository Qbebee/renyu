from django.apps import AppConfig
from django.db.models import BigAutoField

class RyrackConfig(AppConfig):
    verbose_name = '仁宇业务数据'
    name = 'ryRack'
    default_auto_field = BigAutoField
