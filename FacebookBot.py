import urllib.parse
import requests
import facebook

access_token = 'EAAC7yeYE0KUBAOJBGGAnSBFsGyFmFdjZArDN3VqUpBJJqcL39XmN0vP6s8XnCTe4yKBpfxZB2EZA1lmCMUIhSCxrbIaMM02rewxkhCtZA6CifWHbmwLGXBg5ZAETE2X5XMEjkFIrJMiQP9bNSlXTN1yQ21ZC4dLp4OLsCnerNrLgZDZD'

# Set up the Facebook Graph API client
graph = facebook.GraphAPI(access_token=access_token, version='3.1')

# Log in to your Facebook account
# user = graph.get_object('me')
# print("User object is: ",user)

token=graph.get_app_access_token(
    '206475821895845', 'f33a8cbc98a193a0c1a59f1cc4a6d4ca',True)
print(token)

# Create a new post on your Facebook profile
post = graph.put_object('me', 'feed',
                        message='This is a test post created using the Facebook Graph API.')

# post = 'This is an automatic test post'

# link = urllib.parse.urlencode({"message": post, "access_token": access_token})
# response = requests.post(f"https://graph.facebook.com/me/feed/?{link}")

# # post.replace(' ', '+')
# # link = "https://graph.facebook.com/me/feed/?message=" + post + "&access_token=" + access_token
# # response=requests.post(link)
# print(link)
# print(response)
