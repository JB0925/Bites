class JsObject(dict):
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.table = {**kwargs}
        for k, v in kwargs.items():
           self.__dict__[k] = v

    def __getattr__(self, key):
        return self.get(key)
    

    def __getitem__(self, key):
        return self.get(key)


    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.__dict__.update({key:value})


    def __setattr__(self, key, value):
        self.__setitem__(key, value)


    def __delitem__(self, key):
        super().__delitem__(key)
        del self.__dict__[key]


    def __delattr__(self, key):
        self.__delitem__(key)


    def __len__(self):
        return len(self.__dict__)

j = JsObject(a=1, b=2, c=3)
print(j.a)
print(j['a'])
j['d'] = 4
print(j)
del j['d']
print(j)
print(len(j))
j.d = 4
print(j)
del j.d
print(j)
j.d = JsObject(e=5)
print(j.d.e)
j.d.e = JsObject(f=6)
print(j.d.e.f)
