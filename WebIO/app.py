from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
import os


def App():
    f = open(fn, 'rb')
    popup('Hi this is a test',put_text('Learn Python').onclick(lambda:toast('This is a Toast')))
    put_html(f.read())

fn = os.path.join(os.getcwd(), 'webio\\register.html')
print(fn)
start_server(App, port=53976,debug=True)
