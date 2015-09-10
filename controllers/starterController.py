import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import sys
from libs.config import config


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("layout.html")

class StopTornado(tornado.web.RequestHandler):
    @tornado.web.addslash
    def get(self):
        self.write("In StopTornado " + config("PORT"))

class ReturnQuery(tornado.web.RequestHandler):
    def get(self):
        self.write("In ReturnQuery")