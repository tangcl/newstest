import time
from sqlalchemy.sql.expression import desc
from dbmanager import DbManager
from dbtables import *
class NewsDao(object):
    def getSession(self):
        dbManager = DbManager.getInstance()
        if dbManager:
            return dbManager.getSession()
        else:
            return None



    def insert_to_db(self, news):
        session = self.getSession()
        try:
            session.add(news)
            session.commit()
            return True
        except Exception, e:
            session.rollback()
            return False

    def get_news_byname(self, name):
        session = self.getSession()
        try:
            return session.query(News).filter_by(username=name).order_by(desc(News.create_date)).all()
        except Exception, e:
            session.rollback()
            return []

    def get_news_byId(self, id):
        session = self.getSession()
        try:
            return session.query(News).filter_by(id=id).first()
        except Exception, e:
            session.rollback()
            return []

    def get_news_byCategory(self, category_content):
        session = self.getSession()
        try:
            return session.query(News).filter_by(category=category_content).order_by(desc(News.create_date)).all()
        except Exception, e:
            session.rollback()
            return []

    def change_status(self, id, status):
        session = self.getSession()

        try:
            news = session.query(News).filter_by(id=id).first()
            news.status = status
            session.add(news)
            session.commit()
            return True
        except Exception, e:
            session.rollback()
            return False

    def get_news(self):
        session = self.getSession()
        try:
            news = session.query(News).filter_by(status=2).order_by(desc(News.create_date)).all()
            return news
        except Exception, e:
            session.rollback()
            return False