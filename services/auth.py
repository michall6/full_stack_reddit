import requests
import os
from dotenv import load_dotenv

def auth_headers(): 
   
 REDDIT_CLIENT_ID=os.environ['REDDIT_CLIENT_ID']

 REDDIT_SECRET_KEY=os.environ['REDDIT_SECRET_KEY']

 auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_SECRET_KEY)

 data={
        'grant_type':'password',
        'username':os.environ['REDDIT_USER_NAME'],
        'password':os.environ['REDDIT_PASSWORD']
    }
 headers={'User-Agent':'MyAPI/0.0.1'}

 res=requests.post('https://www.reddit.com/api/v1/access_token',
                  auth=auth,data=data,headers=headers)
 
 token=res.json()['access_token'] 

 headers['Authorization'] = f'bearer {token}'
    
 return headers
