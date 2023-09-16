def detectUser(user):
    redirectUrl = None 

    switch_role = {
        1: 'vendorDashboard',
        2: 'custDashboard'
    }

    if user.role in switch_role:
        redirectUrl = switch_role[user.role]
    elif user.role is None and user.is_superadmin:
        redirectUrl = '/admin'

    return redirectUrl
