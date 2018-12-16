from django.contrib.gis.geoip2 import GeoIP2

def user_location(request):
	g = GeoIP2()
	#ip = request.META.get('REMOTE_ADDR', None)
	ip = '103.255.5.60'

	try:
		request.session['COUNTRY'] = g.country(ip)['country_name']
		request.session['CITY'] = g.city(ip)['city']
	except:
		request.session['COUNTRY'] = 'global'
		request.session['CITY'] = ''

	return {}