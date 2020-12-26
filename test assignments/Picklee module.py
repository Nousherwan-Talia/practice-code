import pickle
# #pickling a python object
# car=["audi","bmw","maruti","suzuki","honda"]
# file="mycar.pkl"
# fileobj=open(file,'wb')
# pickle.dump(car,fileobj)
# fileobj.close()

#depickling the object...
#because you cannot read the file in binary text form.....
file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))