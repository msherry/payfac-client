from __future__ import unicode_literals

from communications import Communications
from response import payfacResponse


class payfacRequest(object):

    def __init__(self, config):
        self.config = config
        self.user = config.getUser()
        self.password = config.getPassword()
        self.url = config.getUrl()
        self.communications = Communications(self.user,
                                             self.password,
                                             self.url)

    def sendRequest(self, xml):
        responseXML = self.communications.http_post(xml)
        return payfacResponse(responseXML)
