import requests

# NSFW
any_joke = "https://v2.jokeapi.dev/joke/Any"
response_any = requests.get(any_joke)

if "joke" in response_any.json():
    print(response_any.json()["joke"])
else:
    print("{} {}".format(response_any.json()["setup"], response_any.json()["delivery"]))


# SFW
sfw_joke = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
response_sfw = requests.get(sfw_joke)


if "joke" in response_sfw.json():
    print(response_sfw.json()["joke"])
else:
    print("{} {}".format(response_sfw.json()["setup"], response_sfw.json()["delivery"]))
