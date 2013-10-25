from . import payfacv6XMLFields

class payfacResponse(object):

    def __init__(self, xml_resp):
        self.xml_resp = xml_resp
        self.tree = payfacv6XMLFields.CreateFromDocument(xml_resp.encode('UTF-8'))

    @property
    def id(self):
        self.tree.legalEntityId

    @property
    def code(self):
        """
        text that correlates from .description
        '10': Approved,
        '20': Manual Review,
        '30': Retry,
        '35': Manual Review,
        '36': Duplicate,
        '40': Declined,
        '99': Manual Review - Background Check Error
        """
        return self.tree.responseCode

    @property
    def description(self):
        return self.tree.responseDescription

    @property
    def match(self):
        return self.code == 10
