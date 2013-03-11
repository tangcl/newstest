#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

class Sha1Utils(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod    
    def getsha1( content ):
        sha1obj = hashlib.sha1()
        sha1obj.update(content)
        hash = sha1obj.hexdigest()
        return hash
    
    @staticmethod    
    def getUdid( imei, mac ):
        imei = imei if imei else ''
        mac = mac if mac else ''
        content = imei + mac
        sha1obj = hashlib.sha1()
        sha1obj.update(content)
        hash = sha1obj.hexdigest()
        return hash
    
    @staticmethod 
    def calcMD5(content):
        md5obj = hashlib.md5()
        md5obj.update(content)
        hash = md5obj.hexdigest()
        return hash
    
if __name__ == '__main__':
    imei = '358001046019614'
    print Sha1Utils.getUdid(imei,None)
#    print Sha1Utils.calcMD5('000000000000001000000000000001')