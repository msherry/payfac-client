from __future__ import unicode_literals

import requests


class Communications(object):

    def __init__(self, config):
        self.url = config.getUrl()
        self.auth = (config.getUser, config.getPassword())

    def http_post(self, post_data):
        headers = {
            'Content-type': 'application/com.litle.psp-v6+xml'
        }
        req = requests.post(
            self.url,
            data=post_data,
            auth=self.auth,
            headers=headers
        )
        return req.text
