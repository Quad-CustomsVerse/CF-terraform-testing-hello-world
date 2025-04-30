import functions_framework


# testing CI/CD
@functions_framework.http
def hello_world(request):
    return 'Hello World!', 200
