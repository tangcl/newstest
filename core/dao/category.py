#! -*- encoding:utf-8 -*-
__author__ = 'CLTANG'
import time
from dbmanager import DbManager
from dbtables import *
class CategoryDao(object):
    def getSession(self):
        dbManager = DbManager.getInstance()
        if dbManager:
            return dbManager.getSession()
        else:
            return None

    def list_category(self):
        #查询出所有的分类列表
        self.session = self.getSession()
        try:
            category = self.session.query(CCategory).all()
            return category
        except Exception, e:
            print e
            self.session.rollback()

    def get_category(self, id):
        self.session = self.getSession()
        try:
            category = self.session.query(CCategory).filter_by(id=id).first()
            return category
        except Exception, e:
            print e
            self.session.rollback()
