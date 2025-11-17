# I am going to get the push data of my python_devops repo using python
import requests

url = f"https://api.github.com/repos/AmeerSohail98/python_devops/events"
response = requests.get(url)
pd = response.json()

# print(pd[0]['actor']['login'])  # prints the login of the actor who made the push
count = 0
for i in range(len(pd)):
    # print(pd[i]['actor']['login']) # name of push actor
    count += 1
print(f"Total Push Events: {count}") # push events count by ameer sohail