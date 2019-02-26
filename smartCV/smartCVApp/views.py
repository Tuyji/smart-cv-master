# Create your views here.
from smartCV.smartCVApp.models import AccessToken
import ProfilePdf 
import datetime
import datetime
import oauth2 as oauth
import linkedapi
import urlparse
from django.http import HttpResponse


def home(request):
	return HttpResponse('Well come to smartCV app web page')

def start_session(request):
	 consumer = oauth.Consumer(linkedapi.consumer_key, linkedapi.consumer_secret)
         client = oauth.Client(consumer)
	 content = linkedapi.make_request(client,linkedapi.request_token_url,{},"Failed to fetch request token","POST")
	 request_token = dict(urlparse.parse_qsl(content))
	 AccessToken.objects.filter(token_status=1,oauth_token=request_token['oauth_token']).update(token_status=0)
         a_token= AccessToken()
	 a_token.oauth_token=request_token['oauth_token']
	 a_token.oauth_token_secret=request_token['oauth_token_secret']
	 a_token.created_date=datetime.datetime.now()
	 a_token.token_status=1
	 a_token.save()
         dest_auth_url =str(linkedapi.authorize_url)+"?oauth_token="+str(request_token['oauth_token'])
         return HttpResponse(dest_auth_url)

def grant_session(request):
	request_token=request.GET.get('oauth_token','')
	oauth_verifier=request.GET.get('oauth_verifier',0)
	a_token=AccessToken.objects.get(token_status=1,oauth_token=request_token)

        access_token=linkedapi.get_access_token(request_token,a_token.oauth_token_secret,oauth_verifier)
        a_token.a_oauth_token=access_token['oauth_token']
	a_token.a_oauth_token_secret=access_token['oauth_token_secret']
	a_token.oauth_verifier=oauth_verifier
	a_token.save()
     	response=get_profile_response(request_token)
	return response

def start_granted_session_data(request):
	request_token = request.GET.get('oauth_token','')
        response=get_profile_response(request_token)
	return response

def get_profile_response(request_token):
	json_data=linkedapi.get_profile_data(request_token,'json')
	profile=li.Profile(json_data)
	response = HttpResponse(mimetype='application/pdf') 
	response['Content-Disposition'] = 'attachment; filename="%s"'%(profile.f_name+'_'+profile.l_name)
	pdf=ProfilePdf(profile,response)
	response=pdf.build_profile()
        return response 
