from __future__ import unicode_literals


class Configuration(object):

    def __init__(self):
        self._url = 'cert'

    def setUser(self, user):
        self._user = user

    def setPassword(self, password):
        self._password = password

    def getUrl(self):
        return self._urlMapper(self._url)

    def setUrl(self, url):
        self._url = url

    def _urlMapper(self, target):
        if (target.lower() == "cert"):
            return 'https://some.uri.here'
        elif(target.lower() == "prod"):
            return 'https://psp.litle.com/'
        else:
            return target
