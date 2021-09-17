from django.http import HttpResponse


def verifyParam(*param):
    def verify(func):
        def isNone(request, *args, **kwargs):
            request_parse = getattr(request, request.method)
            for i in param:
                value = request_parse.get(i, None)
                if not value:
                    return HttpResponse("参数错误!!")
                else:
                    return func(request, *args, **kwargs)

        return isNone

    return verify
