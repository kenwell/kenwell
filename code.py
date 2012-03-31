import web
import os
import sys

urls = (
    '/about', 'about',
    '/.*', 'index'
)

curdir = os.path.dirname(__file__)
render = web.template.render(os.path.join(curdir,'templates'))
class index:
    def GET(self):
        return render.index()

class about:
    def GET(self):
        return render.about()
application = web.application(urls, globals()).wsgifunc()

