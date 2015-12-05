from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
import urllib
import requests

#http://shapebootstrap.net/item/1524990-cyprass-html5-responsive-business-template/live-demo
#http://shapebootstrap.net/item/1524954-kadmin-free-responsive-admin-dashboard-template/live-demo

########## GLOBAL VARIABLES ##########
twitchClientId = 'jxjy5g4eoo0idnkp4rqi567xjbkfan9'
twitchClientSecret = 'lgqfpl9if80lyu3hsdvo5zy05b6h5ur'
twitchRedirectUri = 'http://localhost:5000/twitchLoginLanding'
twitchState = 'randomVariables'

########## PAGE MAPS ##########
def landing(request):
	return render(request, 'index.html')


#### BEGINNING OF TWITCH LOGIN ####
def loginViaTwitch(request):
	scope = 'user_read'+'+'+'user_blocks_read'+'+'+'channel_read'+'+'+'channel_commercial'+'+'+'channel_subscriptions'+'+'+'user_subscriptions'+'+'+'channel_check_subscription'+'+'+'chat_login'
	url = 'https://api.twitch.tv/kraken/oauth2/authorize?response_type=code&client_id=%s&redirect_uri=%s&scope=%s&state=%s' % (twitchClientId, twitchRedirectUri, scope,  twitchState)
	return HttpResponseRedirect(url)

def twitchLoginLanding(request):
	if request.GET['code']:
		code = request.GET['code']
		url = 'https://api.twitch.tv/kraken/oauth2/token'
		data = {'client_id':twitchClientId, 'client_secret':twitchClientSecret, 'grant_type':'authorization_code', 'redirect_uri':twitchRedirectUri, 'code':code, 'state':twitchState}
		r = requests.post(url, json=data)
		if r.status_code == 200:
			json_object = r.json()
			accessToken = json_object['access_token']
			refreshToken = json_object['refresh_token']

			# Save token # TBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBD

			# Make call with access_token #
			headers = {"Authorization":'OAuth '+accessToken}
			url = 'https://api.twitch.tv/kraken/user'
			r = requests.get(url, headers=headers)
			return HttpResponse(r.text)
		else:
			return HttpResponse('Error - non 200 status code')
	else:
		return HttpResponse('Error - no code provided')

#### END OF TWITCH LOGIN ####



########## OTHER/ALGORITHMS/RECOMMENDATIONS ##########
def turnSubscriptionsViewsAndFollowersToRevenue(subscriptions,views,followers):
	# Some estimations here # TBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBDTBD
	return revenue