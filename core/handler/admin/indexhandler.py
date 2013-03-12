#! -*- encoding:utf-8 -*-
import time
from core.dao.dbtables import News
from core.dao.news import NewsDao
import json
import tornado

__author__ = 'tangcl'
from core.handler.baseHandler import BaseHandler
from utils.sha1utils import Sha1Utils
from core.dao.tuser import UserDao
from core.dao.category import CategoryDao

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_all_cookies()
        return self.redirect("/admin/login")

class RegisterHandler(BaseHandler):
    def get(self):
        return self.render("register.html", sign=True)

    def post(self):
        #username, userpassword, check in databases
        username = self.get_argument("username")
        password = self.get_argument("password")
        password_md5 =Sha1Utils.calcMD5(password)
        user = UserDao()
        sign = user.register(username, password_md5)
        if sign == 1:
            #注册成功,设置cookie
            self.set_secure_cookie("user", username)
            return self.redirect("/admin/login")
        elif sign == 2:
            #该用户名的用户已经重复
            return self.render("register.html", sign = 2)
        else:
            #注册失败,.
            return self.render("register.html", sign = 3)

class ModeleAjaxHandler(BaseHandler):
    def get(self, model):
        super(ModeleAjaxHandler, self).get()
        return self.write({"model":model})

class CategoryAjaxHandler(BaseHandler):
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

class StatusAjaxHandler(BaseHandler):
    def get(self, id, status):
        super(StatusAjaxHandler, self).get()
        newsdao = NewsDao()
        newsdao.change_status(id, status)
        return self.redirect("/admin/login")

class ArticleAjaxHandler(BaseHandler):
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


class AdminIndexHandler(BaseHandler):
    def get(self):
        super(AdminIndexHandler, self).get()
        username = self.get_current_user()
        return self.render("adminindex.html", user_name=username, sign = 0)

    def post(self):
        #username, userpassword, check in databases
        username = self.get_argument("username")
        password = self.get_argument("password")
        password_md5 =Sha1Utils.calcMD5(password)
        user = UserDao()
        sign = user.find_user(username, password_md5)
        if sign:
            #登录成功,设置cookie
            self.set_secure_cookie("user", username)
            return self.render("adminindex.html", user_name = username)
        else:
            #登录失败.
            return self.render("login.html", sign = False)

