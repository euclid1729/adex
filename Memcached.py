import memcache
IP='127.0.0.1'
PORT='11211'
table="name of cookie table in mysql db"
class Memcached(object):
 mc=None
 dbapi=None
 def __init__(self,ip=IP,port=PORT):
  self.mc = memcache.Client([ip+':'+port], debug=0)
  self.dbapi=#get the singleton db object here 
 #mc.set(key,value) and mc.get(key) are used to fetch data
 def getval(self,key):
  val=self.mc.get(key)
  if not val:
   val=self.dbapi.getval(key,table)
   self.mc.set(key,val)
  return val
 
 def setval(self,key,value):
  self.mc.set(key,value)

 def updateval(self,key,value):
  self.mc.set(key,value)
  #update the db
