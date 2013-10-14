from __future__ import unicode_literals


class legalEntityCreateRequest(object):

    def __init__(self, config):
        self.config = config
        self.user = config.getUser()
        self.password = config.getPassword()

    def sendRequest(self):
        requestXML = self._requestToXml()
        url = self.config.getUrl()
        responseXML = self.communications.http_post(requestXML, url=url)
