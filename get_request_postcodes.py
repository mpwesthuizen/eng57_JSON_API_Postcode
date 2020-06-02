# 1st we need a way to talk http
# we'll use the requests package that is very stable and widely used

# this is a standard py libray no need to install:
#
# import time
#
# time.sleep(1)

# requests is not a standard library and must be install with a packages manager
    #

import requests

# I want ot make a get request to get more info on my postcode
# I need to check my api documentation
# then build the target url with path and arguments
# then in need to use the package request to make the request
# I will, recieve a JSON that i need to parse into a dictionary

path = 'http://api.postcodes.io/postcodes/'
arguments = 'e147le'

#build url
url_target = path + arguments
print(url_target)

# Make request and capture response
response = requests.get(url_target)

# print(response)

# parsing of getting the dictionary out
# print(response.json())

response_dictionary = response.json()

print(type(response_dictionary))
#
# for key in response_dictionary.keys():
#     print(key)

result_dictionary = response_dictionary['result']

print(result_dictionary)

for key in result_dictionary.keys():
    print(key, 'the values inside is', result_dictionary[key])