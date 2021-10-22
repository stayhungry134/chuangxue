from django.shortcuts import redirect


def login_validation(func):
    def user_pass(request):
        if request.session:
            return func(request)
        else:
            return redirect('userprofile:login')
    return user_pass
