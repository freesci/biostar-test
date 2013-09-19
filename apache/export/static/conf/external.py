#
# import from the main settings then override some of the values
#
from wwwportalmlekozyjestart.settings import *

# this is the authentication module and function in it
EXTERNAL_AUTHENTICATOR_FUNC = 'dummy_auth'

MIDDLEWARE_CLASSES.extend([
    'wwwportalmlekozyjestart.extauth.ExternalAuthenticator',
])
