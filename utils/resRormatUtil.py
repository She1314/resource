from django.http import HttpResponse, JsonResponse

class Email(object):
    SUCCESS = 200, '成功'
    PARAM_ERROR = 401, '参数错误'
    UNKNOWN_ERROR = 403, '其他错误'

    def __init__(self, status = 'SUCCESS', data=''):
        if hasattr(self, status):
            self.status_new = getattr(self, status)
        else:
            self.status_new = self.UNKNOWN_ERROR
        self.code, self.response = self.status_new

    def res(self):
        dic = {'code': self.code}
        if self.response:
            dic['response'] = self.response
        return dic

    def JsonResponse(self):
        return JsonResponse(self.res(), json_dumps_params={'ensure_ascii': False})

