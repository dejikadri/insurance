import datetime


class LogToFileMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        f = open('process_log_file.txt', 'a')
        f.write(view_func.__name__ +','+str(datetime.datetime.now())+'\n')
        f.close()
