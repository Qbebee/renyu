from os import path
from django.apps import AppConfig
from  django.db.models import BigAutoField,AutoField

VERBOSE_APP_NAME = '仁宇业务数据'

def  get_current_app_name(file):
    return path.dirname(file).replace('\\','/').split('/')[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME
    default_auto_field = BigAutoField

default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'
