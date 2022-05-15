import requests
import time

x = 1
url = 'https://www.thispersondoesnotexist.com/image'

number = int(input("How many faces would you like to generate?\n"))

while (x - 1) < number:
  response = requests.get(url)
  file = open("images/image" + str(x) + ".png", "wb")
  file.write(response.content)
  file.close()
  print ("Created " + str(file) + "!")
  x = x + 1
  time.sleep(0.75)
