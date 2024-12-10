import decimal

from rest_framework.response import Response

from user_module.models import User

def check_balance(function_cost):

    def check(func):
        def wrapper(*args):
            user:User=args[0].user
            if user.balance < decimal.Decimal(function_cost):
                return Response({'message':'you dont have enough credit for this function'})
            else:
                return func(*args)
        return wrapper
    return check
