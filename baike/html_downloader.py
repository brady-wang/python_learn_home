import string
import urllib.request
from urllib.parse import quote

__author__ = 'wang'


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        url = quote(url,safe=string.printable)
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()

