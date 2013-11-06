#!/usr/bin/env python
#*-* coding: utf-8 *-*

"""
The unofficial API for Kickass Torrents. ♛
"""

from __future__ import unicode_literals


class Torrent(object):
    """A torrent on Kickass Torrents"""
    def __init__(self, title, url, category, magnet_link,
                 torrent_link, created, size, user, seeders, leechers,
                 upvotes,downvotes):
        super(Torrent, self).__init__()
        self.title = title
        self.url = url
        self.category = category
        self.magnet_link = magnet_link
        self.torrent_link = torrent_link
        self.created = created
        self.size = size
        self.user = user
        self.seeders = seeders
        self.leechers = leechers
        self.upvotes = upvotes
        self.downvotes = downvotes

    def __repr__(self):
        return '<{0} by {1}>'.format(self.title,self.user)

    @property 
    def data(self):
        return self.__dict__