# FastAPI

[![Python application test with Github Actions](https://github.com/sdonatileach/fastapi/actions/workflows/main.yml/badge.svg)](https://github.com/sdonatileach/fastapi/actions/workflows/main.yml)


## Click-by-Click Instructions
1. Create a Repo
     1. Open GitHub ; Profile ; Repositories ; New
     2. Repository name = \"your\_repo\_name\" ; Public ; Add a README file ; click Add .gitignore ; click .gitignore template = python ; Create Repository
2. Create an Environment
     1. Open AWS ; Services ; Cloud9 under &quot;Developer Tools&quot; ; &quot;Create environment&quot;
     2. Once environment has been created, click &quot;Open IDE&quot;
3. Create an SSH Key
     1. Go to command line within environment ; Type &quot;ssh-keygen -t rsa&quot; ; Enter ; Skip the prompt for picking a file in which to save the key by pressing Enter again ; Skip the prompt for entering a passphrase by pressing Enter again
     2. Copy everything after &quot;Your public key has been saved in&quot; which will most likely look like this: /home/ec2-user/-ssh/id\_rsa.pub. DO NOT COPY THE PERIOD AT THE END.
     3. In command line type &quot;cat&quot; and paste what you just copied ; copy everything that is returned
     4. Open GitHub ; Settings ; SSH and GPG keys ; New SSH key ; Title = \"your\_environment\_name\" ; paste what you copied from the command line ; Add SSH key
4. Clone Repo
     1. Open GitHub ; Profile ; Repositories ; \"your\_repo\_name\" ; click Code ; click SSH ; copy the address by clicking the icon on the right that looks like a clipboard
     2. Return to AWS Cloud9 ; in the command line type &quot;git clone&quot; and paste what you copied from GitHub ; Enter ; type &quot;cd&quot; and \"your\_repo\_name\" ; Enter
5. Create virtual environment
     1. In the command line type &quot;python3 -m venv ~/.venv&quot; ; Enter ; type &quot;source ~/.venv/bin/activate&quot; ; Enter
6. Initial project scaffolding
     1. In the command line type &quot;touch&quot; and the below files with a space in between each one:
          1. txt
          2. Makefile
          3. py
          4. test\_main.py
     2. Enter
7. Makefile
     1. In the bottom right of the code screen, click Spaces ; Convert to tabs
     2. Paste the below code chunk.
     3. Save the file.
```
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_main.py

format:
	black *.py

run:
	python main.py

run-uvicorn:
	uvicorn main:app --reload

killweb:
	sudo killall uvicorn

lint:
	pylint --disable=R,C main.py
```
8. requirements.txt
     1. In the bottom right of the code screen, click Spaces ; Convert to tabs
     2. Paste the below code chunk.
     3. Save the file.
```
black
fastapi
pytest
pylint
uvicorn[standard]
requests
```
9. Run the above two files simultaneously
     1. Go to the command line ; type &quot;make install&quot; ; Enter
10. Optional Step to alter inbound rules
     1. Open up AWS ; Services dropdown ; click EC2 ; on the left bar Security Groups ; click check box by your FastAPI environment ; Inbound rules ; Edit inbound rules ; Add rule ; Custom TCP&quot; ; Port range = &quot;8080&quot; ; &quot;0.0.0.0/0&quot; ; Save rules
11. Find an API
     1. You&#39;ll need to search for previously built APIs, and [Postman](https://www.postman.com/) is a good site to find them.
     2. Save the URL provided for the API information you need.
     3. This will be used in the next steps.
12. test\_main.py
     1. Go back to Cloud9 ; On the left, double click on the file called &quot;test\_main.py&quot;
     2. Paste the below code chunk.
     3. Replace anything inside brackets with information specific to the API you chose.
     4. Save the file.
```
import requests

def Ping():
    <variable_name> = "<Add your API url here>"
    <response> = requests.get(<variable_name>)
    
    try:
	print(<response>.json()["<Add API column name(s) here>"])
    
    except ValueError:        
        return "Link is unavailable"
        
def test_link_check():    
    assert Ping() != 'Link is unavailable'
```
13. main.py
     1. On the left, double click on the file called &quot;main.py&quot;
     2. Paste the below code chunk.
     3. Replace anything inside brackets with information specific to the API you chose.
     4. Save the file.
     5. Go to the command line ; type &quot;python main.py ; Enter
          1. This will activate your FastAPI
          2. Any time you want to deactivate it, go to the command line and press ctrl + c
```
from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "<Add your message here>"}


@app.get("/<Add API service name here>")
async def <Add API service name here>():

    <variable_name> = "<Add your API url here>"
    <response> = requests.get(<variable_name>)

    print(<response>.json()["<Add API column name(s) here>"])

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
```
14. Commit changes to GitHub
     1. Go to the command line ; ensure you are still in the repo by typing &quot;pwd&quot; ; once confirmed, type &quot;git add&quot; and the below files with a space in between each one
          1. txt
          2. Makefile
          3. py
          4. test\_main.py
     2. Type &quot;git commit -m \"Add your message here\"&quot; ; type &quot;git push&quot;
15. Swagger UI
     1. Return to Cloud9 ; At the top click Preview ; Preview Running Application ; in the bottom right screen, go to the small address bar ; move cursor at the end of the line ; after the forward slash, add what you chose as your &quot;\"API service name\"&quot; ; Enter
     2. Click the box with an arrow on the right to pop out into new window
     3. In the address bar, remove everything after the forward slash, and type &quot;docs&quot;
     4. Click the drop down for \"your API service name\" ; click Try it out ; enter arguments if necessary ; click Execute
16. Configure Build Server
     1. Go to GitHub ; navigate to the repo you created earlier ; click Actions ; click New Workflow ; click set up a workflow yourself at the top of the page
     2. Delete everything inside the &quot;main.yml&quot; file ; Paste the below code chunk.
     3. Click Start commit ; Click Commit new file
     4. Click Actions at the top again ; click the name of the first workflow ; click build ; wait for all actions to have a gray check mark ; click the three dots in the top right
     5. Click create status badge ; click Copy status badge Markdown ; click on the repo name at the top of the page ; open README.md ; click the pen button to edit ; paste the status badge at the top ; scroll down and click Commit changes
```
# Python application test with Github Actions

name: Python application test with Github Actions

# Controls when the workflow will run
on: [push]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v2
      - name: Set up Python 3.8
        uses: actions/setup-python@v1
        with:
          python-version: 3.8
      - name: Install dependencies
        run: |
          make install
      
      - name: Install pyinstall
        run: |
          pip install pytest          
          
      - name: Lint with pylint
        run: |
          make lint
      - name: Test with pytest
        run: |
          make test
```     
17. App Runner
     1. Open AWS ; Services ; App Runner ; Create service
     2. Source code repository ; Add new ; in Connection name, type &quot;Fast API&quot; ; add another ; select GitHub account where your repo lives ; type password ; scroll to Repository access ; Only select repositories ; select your repo ; Save
     3. Select the drop downs and ensure these point to your repo ; Next ; Configure all settings here ; Runtime = Python 3 ; in Build command type &quot;pip install -r requirements.txt&quot; ; in Start command type &quot;python main.py&quot; ; Port = 8080 ; Next ; Type your service name ; Next ; scroll to the bottom and click Create &amp; deploy ; wait approximately 10 minutes for the service to be created
     4. After created, click Configuration tab ; In the first section titled Source and deployment, click Edit on the right ; under Deployment settings click Automatic
     5. Click deploy ; wait approximately five minutes for the service to deploy ; under Default domain, click the url ; repeat steps 15.iii and 15.iv.
