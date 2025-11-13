#To set environment variables in linux we can reun the following command in linux,:  export "varaible name" == "sohail"
#(For the windows this the following $env:password = 'password')
'''We can use os module to check the environment variables data 
--->To check env variables in powershell "Get-ChildItem Env:" command is useful in the terminal'''

import os

result =os.getenv("apitoken")
pwd = os.getenv("password")
print(pwd)
print(result)