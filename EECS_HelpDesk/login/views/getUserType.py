from django.apps import apps

def getUserType(username):
    # helper function that returs the User Type when passed a username
    Student = apps.get_model("login", "Student")
    Admin = apps.get_model("login", "Admin")
    ECHandler = apps.get_model("login", "ECHandler")
    TechnicalFaultHandler = apps.get_model("login", "TechnicalFaultHandler")

    if len(Student.objects.filter(pk=username)) == 1:
        return Student.__name__

    elif len(Admin.objects.filter(pk=username)) == 1:
        return Admin.__name__

    elif len(ECHandler.objects.filter(pk=username)) == 1:
        return ECHandler.__name__

    elif len(TechnicalFaultHandler.objects.filter(pk=username)) == 1:
        return TechnicalFaultHandler.__name__

    return None