from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Add to the url NSFW or SFW"}


@app.get("/NSFW")
async def NSFW():

    any_joke = "https://v2.jokeapi.dev/joke/Any"
    response_any = requests.get(any_joke)

    if "joke" in response_any.json():
        return response_any.json()["joke"]
    else:
        return "{} {}".format(
            response_any.json()["setup"], response_any.json()["delivery"]
        )


@app.get("/SFW")
async def SFW():

    sfw_joke = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    response_sfw = requests.get(sfw_joke)

    if "joke" in response_sfw.json():
        return response_sfw.json()["joke"]
    else:
        return "{} {}".format(
            response_sfw.json()["setup"], response_sfw.json()["delivery"]
        )


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
