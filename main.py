import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import sys
from libs.config import config
from controllers import starterController
from middleware import middleware

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", starterController.MainHandler),
            # Add more paths here
            (r"/KillTornado/?", starterController.StopTornado),
            (r"/tables/", starterController.ReturnQuery)
        ]
        settings = {
            "debug": True,
            "template_path": os.path.join("./", "views/template"),
            "static_path": os.path.join("./", "views/static")
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    # compiling SCSS
    middleware.compileScss()
    
    # ####################
    application = Application()

    print "Listening on port 5000"
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)

    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()