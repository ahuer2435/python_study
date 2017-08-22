d = {'Michael': 95, 23: 75, 'Tracy': 85}
print d['Michael']
d['Michael'] = 91
print d['Michael']
print "Michael" in d
print "Michal" in d
#print 'd.get("Michael") = ' d.get("Michael")
print d.get("Michael",22)
print d.get("Michal",88)
print d.pop("Michael")
print d.get("Michael",22)
print d[23]