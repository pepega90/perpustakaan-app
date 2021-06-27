from django.conf import settings

def user_is_authenticated(req):
	if req.user.is_authenticated:
		return True
	return False