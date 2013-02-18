from __future__ import generators
import time
from heapq import heappush, heappop, heapify

__version__ = "1.0"
__all__ = ['CacheKeyError', 'LRUCache', 'DEFAULT_SIZE']
__docformat__ = 'reStructuredText en'

DEFAULT_SIZE = 1000000
"""Default size of a new LRUCache object, if no 'size' argument is given."""
class SingletonCacheCookie( object ):
    ## Stores the unique Singleton instance-
    _lruCacheInstance = None
    
    class CacheKeyError(KeyError):
#Error raised when cache requests fail 
    
    
     pass
    ## Class used with this Python singleton design pattern
    #this sub class will contain all functionality of LRU Cache 
    class LRUCache(object):
      
      #this class will take care of the Least Recently Used Mechanism via implementing a min heap  
     class __Node(object):
#"""Record of a cached value. Not for public consumption."""
        
        def __init__(self, key, obj, timestamp):
            object.__init__(self)
            self.key = key
            self.obj = obj
            self.atime = timestamp
            self.mtime = self.atime
      
        def __cmp__(self, other):
            return cmp(self.atime, other.atime)

        def __repr__(self):
            return "<%s %s => %s (%s)>" % \
                   (self.__class__, self.key, self.obj, \
                    time.asctime(time.localtime(self.atime)))
     
     #initializing the LRUCache object
     def __init__(self, size=DEFAULT_SIZE):
        # Check arguments
        if size <= 0:
            raise ValueError, size
        elif type(size) is not type(0):
            raise TypeError, size
        object.__init__(self)	
        self.__heap = []
        self.__dict = {}
        self.size = size
     
     def __len__(self):
        return len(self.__heap)
     
     def __contains__(self, key):
        return self.__dict.has_key(key)
     
     def __setitem__(self, key, obj):
        if self.__dict.has_key(key):
            node = self.__dict[key]
            node.obj = obj
            node.atime = time.time()
            node.mtime = node.atime
            heapify(self.__heap)
        else:
            # size may have been reset, so we loop
            while len(self.__heap) >= self.size:
                lru = heappop(self.__heap)
                del self.__dict[lru.key]
            node = self.__Node(key, obj, time.time())
            self.__dict[key] = node
            heappush(self.__heap, node)
     
     def __getitem__(self, key):
        if not self.__dict.has_key(key):
            raise CacheKeyError(key)
        else:
            node = self.__dict[key]
            node.atime = time.time()
            heapify(self.__heap)
            return node.obj
     
     def __delitem__(self, key):
        if not self.__dict.has_key(key):
            raise CacheKeyError(key)
        else:
            node = self.__dict[key]
            del self.__dict[key]
            self.__heap.remove(node)
            heapify(self.__heap)
            return node.obj
     
     def __iter__(self):
        copy = self.__heap[:]
        while len(copy) > 0:
            node = heappop(copy)
            yield node.key
        raise StopIteration
     
     def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        # automagically shrink heap on resize
        if name == 'size':
            while len(self.__heap) > value:
                lru = heappop(self.__heap)
                del self.__dict[lru.key]
     
     def __repr__(self):
        return "<%s (%d elements)>" % (str(self.__class__), len(self.__heap))
     
     def mtime(self, key):
        """Return the last modification time for the cache record with key.
        May be useful for cache instances where the stored values can get
        'stale', such as caching file or network resource contents."""
        if not self.__dict.has_key(key):
            raise CacheKeyError(key)
        else:
            node = self.__dict[key]
            return node.mtime
      
    # init of Singleton Class
    def __init__( self,size=DEFAULT_SIZE ):
        # Check whether we already have an instance
        if SingletonCacheCookie._lruCacheInstance is None:
            # Create and remember instanc
           SingletonCacheCookie._lruCacheInstance=  SingletonCacheCookie.LRUCache(size)
 
        # Store instance reference as the only member in the handle
        self._EventHandler_instance =  SingletonCacheCookie._lruCacheInstance
     
    def __getattr__(self, aAttr):
        return getattr(self._lruCacheInstance, aAttr)
    
    def __setattr__(self, aAttr, aValue):
        return setattr(self._lruCacheInstance, aAttr, aValue)
        
    def createInstance(self): 
        return self.SingletonCacheCookie._lruCacheInstance
 
