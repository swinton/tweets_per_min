Usage
-----
    In [1]: from tweets_per_min import tweets_per_min
    
    In [2]: from getpass import getpass
    
    In [3]: passwd=getpass()
    Password:
    
    In [4]: tpm=tweets_per_min("YOUR_TWITTER_USERNAME", passwd)
    
    In [5]: tpm
    Out[5]: <generator object at 0x7bb2b0>
    
    In [6]: tpm.next()
    Out[6]: 66300.0
    
Contact
-------
Via [email](http://scr.im/stevie) or even [twitter](http://twitter.com/steveWINton). :)
