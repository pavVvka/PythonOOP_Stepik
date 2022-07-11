class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, "author"))
a = Notes()
#del a.title
print(a.__dict__)
setattr(a, "moloko", 3)
print(a.__dict__)
del a.moloko

