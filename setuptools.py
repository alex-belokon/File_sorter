from setuptools import setup

args_dict = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
def do_setup(args_dict):
    for value in args_dict:
        setup(value)
        print(value)
    
               def do_setup(args_dict):
          
          
        