class Codec(object):
    '''
    # Solution 1: simple.
    #   Simple but not secure. User would be able to manipulate the URL numbers.
    def __init__(self):
        """
        :type url: str
        :rtype: str
        """
        self.urls = []
        
    def encode(self, longurl):
        self.urls.append(longurl)
        return 'http://tinyurl.com/'+str(len(self.urls)-1)

    def decode(self, shorturl):
        return self.urls[int(shorturl.split('/')[-1])]
    '''
    
    # ------------------------------------------------------------------------------ #
    
    # Solution 2: better.
    #   Does not have secureity problem. If have duplicate hash, then the user
    #   can just retry until a unique short URL is found, in which would not need
    #   a long time due to the exterm large amount of possible short URL combinations.
    
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        # Would be able to have only 1 dictionary and have decode() be able to find
        # original long URL with given value. But! that would mean linear search, and
        # the run time would be terrible. So! Use space to keep run time short.
        
    def encode(self, longurl):
        code = ""
        # Produce the random 6 letters short URL.
        for _ in range(6):
            code += random.choice(Codec.letters)
        
        if code not in self.url2code:
            self.url2code[longurl] = code
            self.code2url[code] = longurl
        return "http://tinyurl.com/" + self.url2code[longurl]
        
    def decode(self, shorturl):
        # print shorturl
        # print self.code2url[shorturl]
        # Return the shorturl[-6:], the last 6 letters because only the code was needed
        # to be used in the code2url dictionary to find correct long URL.
        return self.code2url[shorturl[-6:]]
