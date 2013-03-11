#! -*- encoding:utf-8 -*-
import time
from core.dao.dbtables import News
from core.dao.info import InfoDao
from core.dao.news import NewsDao
import json
import tornado
from tornado.escape import utf8, xhtml_unescape
from tornado.util import b

__author__ = 'tangcl'
from cgi import escape
from core.handler.baseHandler import NoneHandler
from utils.sha1utils import Sha1Utils
from core.dao.tuser import UserDao
from core.dao.category import CategoryDao

class ListHandler(NoneHandler):
    @tornado.web.asynchronous
    def get(self):
        super(ListHandler, self).get()
        #查询出分类下的最新20列表数据
        categorydao = CategoryDao()
        categorylist = categorydao.list_category()
        newsdao = NewsDao()
        data = []
        if categorylist:
            #有分类,根据分类查询出改分类的文章.

            for category in categorylist:
                category_dict = {}
                news_list = newsdao.get_news_byCategory(category.content)
                news_json_list = []
                for news in news_list:
                    news_dict = {}
                    news_dict.update({"title":news.title, "create_date":news.create_date, \
                                      "username":news.username, "id":news.id})
                    news_json_list.append(news_dict)
                category_dict.update({"category_id":category.id, "category_content":category.content, "news":news_json_list})
                data.append(category_dict)
        return self.render("index.html", data = {"data":data})

class DetailHandler(NoneHandler):
    @tornado.web.asynchronous
    def get(self, id):
        super(DetailHandler, self).get()
        #获取新闻ID,获取详情
        newsdao = NewsDao()
        news = newsdao.get_news_byId(id)
        #根据新闻ID,查询info信息,如果有,传递数据,没有,返回0
        infodao = InfoDao()
        info = infodao.get_info_by_id(id)
        if info:
            return self.render("detail.html", news = news, info=info)
        else:
            return self.render("detail.html", news = news, info=False)
class CategoryAjaxHandler(NoneHandler):
    @tornado.web.asynchronous
    def get(self):
        super(CategoryAjaxHandler, self).get()
        #查询出当前所有分类
        category_dao = CategoryDao()
        category_list = category_dao.list_category()
        category_json_list = []
        if category_list:
            for category in category_list:
                category_json_list.append({"id":category.id, "content":category.content})
        return self.write({"category":category_json_list})


class SupportAjaxHandler(NoneHandler):
    @tornado.web.asynchronous
    def get(self, news_id, support):
        super(SupportAjaxHandler, self).get()
        #根据文章ID,插入数据
        infodao = InfoDao()
        print "news_id:", news_id
        sign =  infodao.insert_data(news_id, support_id=support)

        if sign:
            self.set_cookie(news_id, support)
            return self.write({"support":support})

class PointAjaxHandler(NoneHandler):
    @tornado.web.asynchronous
    def get(self, news_id, point):
        super(PointAjaxHandler, self).get()
        #根据文章ID,插入数据
        infodao = InfoDao()
        sign =  infodao.insert_data(news_id, point_id=point)
        if sign:
            self.set_cookie("point_cookie", point)
            return self.write({"point":point})


class NewsHandler(NoneHandler):
    @tornado.web.asynchronous
    def get(self):
        super(NewsHandler, self).get()

        newsdao = NewsDao()
        all_news = newsdao.get_news()
        return self.render("newest.html", data = all_news)

class ArticleAjaxHandler(NoneHandler):
    @tornado.web.asynchronous
    def get(self):
        super(ArticleAjaxHandler, self).get()
        username = self.get_current_user()
        newdao = NewsDao()
        news_list = newdao.get_news_byname(username)
        news_json_list = []
        if news_list:
            for news in news_list:
                news_json_dict = {}
                news_json_dict["category"] = news.category
                news_json_dict["title"] = news.title
                news_json_dict["create_date"] = str(news.create_date)
                news_json_dict["content"] = news.content
                news_json_dict["status"] = news.status
                news_json_dict["id"] = news.id
                news_json_list.append(news_json_dict)
        data = {"data": news_json_list}
#        data = json.dumps(data, ensure_ascii=False)
        return self.write(data)

    def post(self):
        super(ArticleAjaxHandler, self).get()
        category_id = self.get_argument("category_id")
        title = self.get_argument("title")
        username = self.get_argument("username")
        content = self.get_argument("content")
        status = self.get_argument("status")
        categorydao = CategoryDao()
        category = categorydao.get_category(int(category_id))
        news = News()
        news.category = category.content
        news.title = title
        news.create_date = time.strftime("%Y-%m-%d %H;%M:%S")
        news.status = int(status)
        news.username = username
        news.content = content
        newdao = NewsDao()
        sign = newdao.insert_to_db(news)
        return self.write({"sign":sign})