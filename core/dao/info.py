#! -*- encoding:utf-8 -*-
__author__ = 'CLTANG'
import time
from dbmanager import DbManager
from dbtables import *
from sqlalchemy import desc
from sqlalchemy import or_
from MySQLdb import IntegrityError
class InfoDao(object):
    def getSession(self):
        self.dbManager = DbManager.getInstance()
        if self.dbManager:
            return self.dbManager.getSession()
        else:
            return None


    def __del__(self):
        self.dbManager.removeSession()

    def insert_data(self, news_id, support_id=0, point_id=0):
        self.session = self.getSession()
        try:
            info = self.session.query(Info).filter_by(news_id=news_id).first()
            if info:
                if support_id == 0:
                    #更新踩一下数据
                    info.point_id = point_id
                    self.session.add(info)
                    self.session.commit()
                elif point_id == 0:
                    #更新顶一下数据
                    info.support_id = support_id
                    self.session.add(info)
                    self.session.commit()
                else:
                    #逻辑上不可能2个都等于0却调用此接口
                    return False
                return True
            else:
                #当前没有数据
                info = Info()
                info.news_id = news_id
                info.support_id = support_id
                info.point_id = point_id
                self.session.add(info)
                self.session.commit()
                return True
        except Exception, e:
            print e
            return False

    def get_info_by_id(self, news_id):
        self.session = self.getSession()
        try:
            info = self.session.query(Info).filter_by(news_id=news_id).first()
            return info
        except:
            return False