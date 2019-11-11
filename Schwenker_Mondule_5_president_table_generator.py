import os, os.path

import pandas as pd
import io
import requests

import cherrypy

class ExposeTable(object):
    @cherrypy.expose
    def index(self):
        presidents_url = "https://raw.githubusercontent.com/charleyferrari/CUNY_DATA_608/master/module5/data/presidents.csv"
        s=requests.get(presidents_url).content
        presidents=pd.read_csv(io.StringIO(s.decode('utf-8')))
        html = presidents.to_html()
        return html

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
    cherrypy.config.update({'server.socket_port': 8082})
    cherrypy.quickstart(ExposeTable(), '/', conf)