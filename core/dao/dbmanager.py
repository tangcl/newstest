#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mar 22, 2012

@author:
"""
import time
import ConfigParser
import hashlib
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import and_, or_
import os
import logging
from core.dao.dbtables import *
from sqlalchemy import desc

ABS_PATH = os.path.dirname(os.path.abspath(__file__))
NQ_CONFIG = ABS_PATH + \
 "/../../config/xylx.conf"
Session = None
class DbManager:
    '''
    管理mysqlalchemy 数据库连接 表映射 和 session 
    '''
    __single = None
    __meta = None
    __mysqlDb = None
    
    def __init__(self):
        if DbManager.__single:
            raise DbManager.__single
        DbManager.__single = self
        
    @staticmethod
    def getInstance():
        '''获取单例 绑定数据源和映射表'''
        if DbManager.__single is None:
            DbManager.__single = DbManager()
            cf = ConfigParser.ConfigParser()
            cf.read(NQ_CONFIG)
            url = "%s://%s:%s@%s/%s?charset=%s" \
                % (cf.get("db", "db_engine"), cf.get("db", "db_user"), \
                cf.get("db", "db_pass"), cf.get("db", "db_host"),  \
                cf.get("db", "db_name"), cf.get("db", "db_charset")
                       )
            ''' 正式环境 不需要设字符集
            url = "%s://%s:%s@%s/%s" \
                % (cf.get("db", "db_engine"), cf.get("db", "db_user"), \
                cf.get("db", "db_pass"), cf.get("db", "db_host"),  \
                cf.get("db", "db_name"))
            '''
            try:
                DbManager.__mysqlDb = create_engine(url,pool_size=20, max_overflow=-1, pool_recycle=7200,echo=True) #
                DbManager.__meta = MetaData()
                DbManager.__meta.reflect(bind=DbManager.__mysqlDb)
                DbManager.bindTables()
                global Session

                #Session = sessionmaker(bind=DbManager.__mysqlDb,autoflush=True)
                Session = scoped_session(sessionmaker(bind=DbManager.__mysqlDb,autoflush=True))
                print Session
            except Exception,e:
                print e,"===db connect error=== DbManager.getInstance()"
                logging.error(e)
                DbManager.__single = None
                raise e

        return DbManager.__single
    
    @staticmethod
    def bindTables():
        '''完成数据库表和domain对象的映射'''
        #bind t_user
        tuser = DbManager.__meta.tables['tuser']
        mapper(TUser, tuser)

        ccategory = DbManager.__meta.tables['ccategory']
        mapper(CCategory, ccategory)

        news = DbManager.__meta.tables['news']
        mapper(News, news)

        info = DbManager.__meta.tables['info']
        mapper(Info, info)

    def getSession(self):
        Session.remove()
        return Session()
    
    def removeSession(self):      
        if Session:
            Session.remove()

class Check_Sql():

    def __init__(self):
        self.dbManager = DbManager.getInstance()
        #如果连接失败 获取实例时会再尝试连接一次
    #    dbManager = DbManager.getInstance()
        if self.dbManager:
            self.session = self.dbManager.getSession()
        else:
            raise

    def find_user(self):
        username = "username"
        password = "password"
        user = self.session.query(TUser).filter_by(id=username, password=password).first()
if __name__=="__main__":
    #测试根据id查询软件信息
    class_test = Check_Sql()
    class_test.find_user()




