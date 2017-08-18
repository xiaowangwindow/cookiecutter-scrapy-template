# -*- coding:utf8 -*-

import pymongo


class MongoManager():
    def __init__(self,
                 host='localhost',
                 port=27017,
                 user=None,
                 password=None,
                 db='admin',
                 auth_mechanism='SCRAM-SHA-1',
                 uri=None):
        if uri:
            self.url = uri
        else:
            self.url = 'mongodb://{account}{host}:{port}'.format(
                account='{username}:{password}@'.format(
                    username=user,
                    password=password) if user is not None else '',
                host=host,
                port=port,
                auth_mechanism=auth_mechanism,
            )
        self.db = db

    def __enter__(self):
        self.client = pymongo.MongoClient(self.url)
        return self.client[self.db]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


if __name__ == '__main__':
    pass
