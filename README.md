This project deals with development of an ad exchange built on Open RTB standards. The main functionality includes 
1. Development of ad redirection from user's browser with request for ad
2. Cookie Syncronization process to get a mapped table of user cookie id with DSP's cookie id.
3. Filtering bids according to DSP's ad campaign specifications
4. Time bouding the Vickery auction procedure in 120 ms.
5. Redirecting user browser with the ad.
6. Global ad/publishers blocked list

We are using Python for the development, Cherrypy for hosting, apart from in memory caches we are also using distributed caching framework, Memcached, to store cookie related information.  


Check123 
