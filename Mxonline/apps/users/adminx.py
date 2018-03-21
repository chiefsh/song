# _*_coding:utf-8_*_
__author__ = 'song'
__date__ = '2017/9/24 20:07'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner,UserProfile

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title="慕学后台管理系统"
    site_footer="慕学在线网"
    menu_style="accordion"   #将菜单栏收起来

class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter =['title', 'image', 'url', 'index','add_time']

#
# class UserProfileAdmin(object):
#     list_display = ['nick_name', 'birthday', 'gender', 'address','mobile','image']
#     search_fields = ['nick_name', 'birthday', 'gender', 'address','mobile','image']
#     list_filter =['nick_name', 'birthday', 'gender', 'address','mobile','image']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)



