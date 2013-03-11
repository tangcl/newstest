#! -*- encoding:utf-8 -*-
__author__ = 'CLTANG'
import time
from dbmanager import DbManager
from dbtables import *
from sqlalchemy import desc
from sqlalchemy import or_
from MySQLdb import IntegrityError
class UserDao(object):
    def getSession(self):
        self.dbManager = DbManager.getInstance()
        if self.dbManager:
            return self.dbManager.getSession()
        else:
            return None

    def update_lastdate(self, name):
        #更新用户使用时间
        self.session = self.getSession()
        try:
            user = self.session.query(TUser).filter_by(name=name).first()
            user.last_date = time.strftime("%Y-%m-%d %H:%M:%S")
            self.session.commit()
        except:
            self.session.rollback()

    def __del__(self):
        self.dbManager.removeSession()

    def register(self, name, password):

        self.session = self.getSession()

        user = self.session.query(TUser).filter_by(name=name).first()
        if user:
            return 2
        try:
            user = TUser()
            user.name=name
            user.password = password
            user.createdate = time.strftime("%Y-%m-%d %H:%M:%S")
            user.last_login = time.strftime("%Y-%m-%d %H:%M:%S")
            self.session.add(user)
            self.session.commit()
            return 1
        except Exception, e:
            print e
            self.session.rollback()
            return 3

    def find_user(self, username, password):
        self.session = self.getSession()
        try:
            user = self.session.query(TUser).filter_by(name=username, password=password).first()
            if user:
                return True
            else:
                return False
        except:
            return False
