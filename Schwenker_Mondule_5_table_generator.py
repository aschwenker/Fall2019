import os, os.path
import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="2" name="length" />
              <button type="submit">Show me Multiples!</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, length=8):
        multiples = range(int(length), (20 * int(length))+1, int(length)) 
        some_table = """<table style="width:100%">
  <tr>
    <th>"""+str(multiples[0])+"""</th>
    <th>"""+str(multiples[1])+"""</th>
    <th>"""+str(multiples[2])+"""</th>
    <th>"""+str(multiples[3])+"""</th>
  </tr>
  <tr>
    <th>"""+str(multiples[4])+"""</th>
    <th>"""+str(multiples[5])+"""</th>
    <th>"""+str(multiples[6])+"""</th>
    <th>"""+str(multiples[7])+"""</th>
  </tr>
  <tr>
    <th>"""+str(multiples[8])+"""</th>
    <th>"""+str(multiples[9])+"""</th>
    <th>"""+str(multiples[10])+"""</th>
    <th>"""+str(multiples[11])+"""</th>
  </tr>
    <tr>
    <th>"""+str(multiples[12])+"""</th>
    <th>"""+str(multiples[13])+"""</th>
    <th>"""+str(multiples[14])+"""</th>
    <th>"""+str(multiples[15])+"""</th>
  </tr>
    <tr>
    <th>"""+str(multiples[16])+"""</th>
    <th>"""+str(multiples[17])+"""</th>
    <th>"""+str(multiples[18])+"""</th>
    <th>"""+str(multiples[19])+"""</th>
  </tr>
</table>"""
        return some_table

    @cherrypy.expose
    def display(self):
        return cherrypy.session['mystring']


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)