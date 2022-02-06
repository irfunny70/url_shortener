import pyshorteners

s = pyshorteners.Shortener()
print(s.tinyurl.short('http://youtube.com/watch?v=0k447K0zx5I'))
print(s.isgd.short('http://www.flexmind.co'))
print(s.osdb.short('http://www.flexmind.co'))
