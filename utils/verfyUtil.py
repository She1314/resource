from django.http import HttpResponse
from utils.resRormatUtil import Email

def verifyParam(*param):
    def verify(func):
        def isNone(request, *args, **kwargs):
            request_parse = getattr(request, request.method)
            for i in param:
                value = request_parse.get(i, None)
                if not value:
                    return Email('PARAM_ERROR').JsonResponse()
                else:
                    return func(request, *args, **kwargs)

        return isNone

    return verify
