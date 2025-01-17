class TimeMap:
    def __init__(self) -> None:
        self.timemap={}
    def set(self, key, value, times):
        if not self.timemap.get(key):
            self.timemap[key]=[{'stamp':times, 'val':value}]
        else:
            self.timemap[key].append({'stamp':times, 'val':value})
    def get(self, key,times):
        
        if not self.timemap.get(key):
            return ''
         
        for i in range(len(self.timemap[key])-1,-1,-1):
            if self.timemap[key][i]['stamp']<=times:
                return self.timemap[key][i]['val']
            else:
                return ''
        #return self.timemap

tm=TimeMap()
tm.set('foo','bar',1)
print(tm.get("foo", 1))       
print(tm.get("foo", 3))        
tm.set("foo", "bar2", 4); 
print(tm.get("foo", 4));         
print(tm.get("foo", 5));