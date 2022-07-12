from django.http import HttpResponse

# test commit


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница')
