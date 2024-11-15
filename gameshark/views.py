from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    context = {
        "message": "A página que você está procurando não foi encontrada."
    }
    return render(request, "errors/404.html", context, status=404)


def handler500(request):
    """ Custom handler for 500 errors """
    return render(request, 'errors/500.html', status=500)