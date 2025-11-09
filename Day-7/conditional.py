import sys
import os

type = sys.argv[1]
ev_var =sys.argv[2]
record = sys.argv[3]

os.environ[ev_var] = record

if type == 't2.micro':
    print('For this service it will cost you 2000/- rupees')
    print(os.getenv(ev_var))
elif type == 't2.medium':
    print('For this service it will cost you 4000/- rupees')
    print(os.getenv(ev_var))
elif type == 't3.large':
    print('For this service it will cost you 8000/- rupees')
    print(os.getenv(ev_var))
else:
    print('Please provide valid instance name')