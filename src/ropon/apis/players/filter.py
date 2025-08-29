def with_auth_token(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        auth_token = kwargs.pop("auth_token", None) 
        instance.auth_token = auth_token  
        return func(*args, **kwargs)
    return wrapper