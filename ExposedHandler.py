import cherrypy
class MainHandler:
    jsonObj=Jsonconvertor()
    listAdvertiser=FilterAdvertisers()
    bidder=Bidder()
    def index(self):
        return ''            
    index.exposed = True
    
    def getad(self, type_of_ad,publisher_id,zone,topic,subtopic,page_keywords,title,slot_ad,size_ad,user_browser,user_os,IP,user_id):
        # CherryPy passes all GET and POST variables as method parameters.
        # It doesn't make a difference where the variables come from, how
        # large their contents are, and so on.
        obj=self.jsonObj.converttojson(type_of_ad,publisher_id,zone,topic,subtopic,page_keywords,title,slot_ad,size_ad,user_browser,user_os,IP,user_id)
        #generating list of advertisers to send bid to
        filteredAdvertiserList=self.listAdvertisers(obj)
        #dictionary of rtb url mapped to their request json, request json is direrent cause user cookie id will be different for each rtb
        requestJsonlist=self.bidder.getdicrequestjson(filteredAdvertiserList,obj)
        self.bidder.startbid(requestJsonlist)
        
        
    greetUser.exposed = True
    
     def bidresponse(self,response):
     
     def cookiesync(self,rtb_id,user_ccokie_id):
      #generate html, embed java script to check if we have a cookie on user's browser, if yes get id else generate new cookie, map the cookie id with rtb_cookie id, update cache, update db 

import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'tutorial.conf')

if __name__ == '__main__':
    cherrypy.quickstart(MainHandler(), config=tutconf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(MainHandler(), config=tutconf)
