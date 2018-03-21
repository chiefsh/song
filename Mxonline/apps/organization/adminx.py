# _*_coding:utf-8_*_
__author__ = 'song'
__date__ = '2017/10/24 23:03'

import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'add_time','click_nums','fav_nums','address','city']
    search_fields =  ['name', 'desc', 'add_time','click_nums','fav_nums','address','city']
    list_filter =  ['name', 'desc', 'add_time','click_nums','fav_nums','address','city']

class TeacherAdmin(object):
    list_display = ['name', 'add_time','org','work_years','work_company','work_position']
    search_fields = ['name',  'add_time','org','work_years','work_company','work_position']
    list_filter = ['name',  'add_time','org','work_years','work_company','work_position']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)