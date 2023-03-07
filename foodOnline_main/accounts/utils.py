
def detectUser(user):
    if user.role == 0:
        redirect_url = 'vendorDashboard'
        return redirect_url
    elif user.role == 1:
        redirect_url = 'custDashboard'
        return redirect_url
    elif user.role is None and user.is_superadmin:
        redirect_url = '/admin'
        return redirect_url
