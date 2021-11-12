import requests

def Ping():
    # NSFW
    any_joke = "https://v2.jokeapi.dev/joke/Any"
    response_any = requests.get(any_joke)  


    # SFW
    sfw_joke = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    response_sfw = requests.get(sfw_joke)
    
    try:
        if "joke" in response_any.json():
            print(response_any.json()["joke"])
        else:
            print("{} {}".format(response_any.json()["setup"], response_any.json()["delivery"]))
            
        if "joke" in response_sfw.json():
            print(response_sfw.json()["joke"])
        else:
            print("{} {}".format(response_sfw.json()["setup"], response_sfw.json()["delivery"]))    
    except ValueError:        
        return "Link is unavailable"
        
def test_link_check():    
    assert Ping() != 'Link is unavailable'
