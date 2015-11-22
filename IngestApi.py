import cherrypy
from subprocess import Popen
import urllib.request
import json
itemAPI = "http://www.boneyard.io/api/specimens/"

class Ingest(object):
    @cherrypy.expose
    def ingest(self,guid):
        Popen(["/usr/bin/python3","BangAndClear.py " + guid])
        return "OK"
    @cherrypy.expose
    def check(self,id):
        try:
            with urllib.request.urlopen(itemAPI) as response:
                specimens = json.loads(response.read)
                for(s in specimens):
                    if("institutional_id" in s.keys):
                        if(s['institutional_id']):
                            raise  cherrypy.HTTPError(500) 
                return "OK"
        except urllib.error.HTTPError as e:
            raise  cherrypy.HTTPError(e.code) 

if __name__ == '__main__':
   cherrypy.quickstart(Ingest(), '/')
