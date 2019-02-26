from smartCV.smartCVApp.models import AccessToken
import oauth2 as oauth
import urlparse

consumer_key    =   'xxxx'
consumer_secret =   'xxxx'
request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken?scope=r_fullprofile+r_emailaddress+r_contactinfo'
access_token_url =  'https://api.linkedin.com/uas/oauth/accessToken'
authorize_url =     'https://api.linkedin.com/uas/oauth/authorize'
dest_url_json ="http://api.linkedin.com/v1/people/~:(id,first-name,last-name,location:(name),summary,headline,picture-url,industry,skills:(skill,proficiency,years),three-past-positions,educations,honors,interests,languages:(id,language,proficiency),three-current-positions,certifications,courses,phone-numbers,main-address,email-address)?format=json"

def get_request_token():
	 consumer = oauth.Consumer(consumer_key, consumer_secret)
	 client = oauth.Client(consumer)
	 content = linkedapi.make_request(client,linkedapi.request_token_url,{},"Failed to fetch request token","POST")
	 request_token = dict(urlparse.parse_qsl(content))
	

def get_access_token(oauth_token,oauth_token_secret, oauth_verifier):
	 consumer = oauth.Consumer(consumer_key, consumer_secret)
	 client = oauth.Client(consumer)
         token = oauth.Token(oauth_token,oauth_token_secret)
         token.set_verifier(oauth_verifier)
         client = oauth.Client(consumer, token)
         content = make_request(client,access_token_url,{},"Failed to fetch access token","POST")
         access_token = dict(urlparse.parse_qsl(content))
         return access_token

# Simple oauth request wrapper to handle responses and exceptions
def make_request(client,url,request_headers={},error_string="Failed Request",method="GET",body=None):
	if body:
		resp,content = client.request(url, method, headers=request_headers, body=body)
	else:
		resp,content = client.request(url, method, headers=request_headers)
	print resp.status
		
	if resp.status >= 200 and resp.status < 300:
		return content
	elif resp.status >= 500 and resp.status < 600:
		error_string = "Status:\n\tRuh Roh! An application error occured! HTTP 5XX response received."
		
	else:
		print 'hata var aq'
	
def get_profile_data(request_tokeni,data_format='json'):
	try:
		a_token_dict=AccessToken.objects.filter(token_status=1,oauth_token=request_token)
		response=''
		if len(a_token_dict) >0:
			try:
				a_token=a_token_dict[0]
				consumer = oauth.Consumer(consumer_key, consumer_secret)
				client = oauth.Client(consumer)
				token=oauth.Token(a_token.a_oauth_token,a_token.a_oauth_token_secret)		
				client= oauth.Client(consumer, token)
				response = make_request(client,dest_url_json)
				data=response
				if data_format=='json':
					data=json.loads(response)

				return data
			except Exception as e:
				return 'o geldi'
		else:
			return('First Grant App')
	except Exception as e:
		return 'Internal error'

