#this program will be running as a separate server on a separate machine, and will be accepting the cookie id mapping from DSP
#DSP will send dsp id and user_dsp_cookie_id as a http redirect from its 0 pixel image redirection from the web page, we will try to get our cookie id from the user's browser and if not present will drop our cookie there 

import cherrypy
import os.path
import random
import Memcached
serverconf = os.path.join(os.path.dirname(__file__), 'server.conf')
class Root:
    cookie_key='dennoo_ad_ex_'
    
    def __init__(self):
     self.memcache=Memcached.Memcached()
     
    def setCookie(self):
        cookie = cherrypy.response.cookie
        cookie_val=random.random()
        val_l=len(str(cookie_val))
        cookie_val=int(cookie_val * 10 **(val_l-2))
        cookie[str(Root.cookie_key) ] = str(cookie_val)
        #cookie['cookieName'] = 'cookieValue'
        return str(cookie_val)
    setCookie.exposed = False

    def cookie_match_request(self,dsp_user_cookie_id,dsp_id):
        cookie = cherrypy.request.cookie
        if  len(cookie) ==0:
         cookie_val=self.setCookie()
         
        else:
         cookie_val=cookie[Root.cookie_key].value
        
        self.update_memcache(cookie_val,dsp_id,dsp_user_cookie_id)
        return str(cookie_val)
    cookie_match_request.exposed = True
    
    def update_memcache(self,cookie_val,dsp_id,dsp_user_cookie_id):
        val=self.memcache.getval(cookie_val)
        
        if val is None: #this is the first time this user os redirected to ad ex
         val={}   

        val[dsp_id]=dsp_user_cookie_id
        self.memcache.setval(cookie_val,val)
        
cherrypy.quickstart(Root(), config=serverconf)
