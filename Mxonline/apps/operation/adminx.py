# _*_coding:utf-8_*_
__author__ = 'song'
__date__ = '2017/10/22 10:52'


import xadmin
from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse

class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name', 'add_time']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']

class CourseCommentsAdmin(object):
    list_display = ['course', 'user', 'add_time','comments']
    search_fields = ['course', 'user', 'add_time','comments']
    list_filter = ['course', 'user', 'add_time','comments']

class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'add_time','fav_type']
    search_fields =  ['user', 'fav_id', 'add_time','fav_type']
    list_filter = ['user', 'fav_id', 'add_time','fav_type']

class UserMessageAdmin(object):
    list_display = ['user', 'message', 'add_time','has_read']
    search_fields =['user', 'message', 'add_time','has_read']
    list_filter = ['user', 'message', 'add_time','has_read']


class UserCourseAdmin(object):
    list_display = ['course', 'user', 'add_time']
    search_fields = ['course', 'user', 'add_time']
    list_filter =  ['course', 'user', 'add_time']



xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)