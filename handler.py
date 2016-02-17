#!/usr/bin/env python
# _*_coding:utf-8_*_

import logging
from datetime import datetime
from socket import gethostname
from pymongo import MongoClient
from bson import InvalidDocument


class MongoFormatter(logging.Formatter):
    def format(self, record):
        """制定需要的日志信息"""
        data = record.__dict__.copy()

        if record.args:
            record.msg = record.msg % record.args
		# 添加需要的信息
        data.update(
            time=datetime.now(),
            message=record.msg,
            args=tuple(unicode(arg) for arg in record.args)
        )
        if 'exc_info' in data and data['exc_info']:
            data['exc_info'] = self.formatException(data['exc_info'])
        return data


class MongoHandler(logging.Handler):
    """ 
	控制类
    """

    @classmethod
    def to(cls, db, collection, host='localhost', port=None, level=logging.NOTSET):
        """ Create a handler for a given  """
        return cls(MongoClient(host, port)[db][collection], level)

    def __init__(self, collection, db='mongolog', host='localhost', port=None, level=logging.NOTSET):
        """ Init log handler and store the collection handle """
        logging.Handler.__init__(self, level)
        if (type(collection) == str):
            self.collection = MongoClient(host, port)[db][collection]
        else:
            self.collection = collection
        self.formatter = MongoFormatter()

    def emit(self, record):
        """ 往mongodb存储日志信息"""
        try:
            self.collection.save(self.format(record))
        except InvalidDocument, e:
            logging.error("Unable to save log record: %s", e.message, exc_info=True)

