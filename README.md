
### A simple experiment measuring the response time of grpc and rpyc

By default it will run 2000 times

#### How to run

1. First install the requirements to your python using pip
```
$ pip install -r requirements.txt
```
Note: I recommend using a python virtual env just to keep the local installation of python clean

2. Then enter the directory name grpc or rpyc with `cd`
3. Execute the server first then the client
Note: You may will need two instances of your terminal since the server will block one when you run it or you can run it in the background with the operator `&` to run it inside the same terminal


##### (Optional) Installing and creating a python virtual env
1. First install the package to allow the creation of a python virtual env, please check your distro repository
2. Then execute the command
```
$ python -m venv venv
```
This should create a directory named "venv"
3. Finally activated
```
$ source venv/bin/activate
```
After using your virtual env you can exit it with the command
```
$ deactivate
```
