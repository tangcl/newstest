#! -*- encoding:utf-8 -*-

__author__ = 'C.L.TANG'
'''
本文件为所有URL路由文件
'''
from core.handler.admin.indexhandler import *
from core.handler.front.indexhandler import *
from tornado.web import ErrorHandler
from tornado import web
application = [
    (r"/static/images/(.*)", web.StaticFileHandler, {"path": "./static"}),
    (r"/register", RegisterHandler),
    (r"/model/ajax/model=(.*)", ModeleAjaxHandler),
    (r"/category/ajax/", CategoryAjaxHandler),
    (r"/artile/ajax/", ArticleAjaxHandler),
    (r"/status/ajax/(.*)/(.*)", StatusAjaxHandler),
    (r"/index/", ListHandler),
    (r"/newest/", NewsHandler),
    (r"/detail/(.*)/", DetailHandler),
    (r"/support/(.*)/(.*)/", SupportAjaxHandler),
    (r"/point/(.*)/(.*)/", PointAjaxHandler),
    (r"/logout", LogoutHandler),
    (r"/admin/login", AdminIndexHandler),
    (r"/error",ErrorHandler),
    (r"/downloadstore/(.*)", web.StaticFileHandler, {"path": "./video/store"}),
    (r"/downloadimg/(.*)", web.StaticFileHandler, {"path": "./video/img"}),
]