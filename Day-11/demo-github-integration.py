'''Creating a python program to get pull reuqest information for a specifc git hub repo (tensorflow/tensorflow)'''
#To connect with ensorflow repo we can use python requests module to connect with api
import requests

result = requests.get('https://api.github.com/repos/tensorflow/tensorflow/pulls')
response=result.json()
print(result.status_code)

#print(response[0]["user"]["login"])
for i in range(len(response)):
    print(response[i]["user"]["login"])

#Tasks-2
