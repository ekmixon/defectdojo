def social_uid(backend, details, response, *args, **kwargs):
    if uid := backend.get_user_id(details, response):
        return {'uid': uid}
    else:
        return {'uid': response.get('preferred_username')}


def modify_permissions(backend, uid, user=None, social=None, *args, **kwargs):
    if kwargs.get('is_new'):
        user.is_staff = True
