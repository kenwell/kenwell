import web
import os
import sys

urls = (
    '/.*', 'index'
)

curdir = os.path.dirname(__file__)
render = web.template.render(os.path.join(curdir,'templates'))
class index:
    def GET(self):
        return render.index()

application = web.application(urls, globals()).wsgifunc()

