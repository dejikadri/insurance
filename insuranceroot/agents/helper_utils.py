from .models import Agent
from passlib.hash import sha512_crypt
from random import randint


def success_msg(msg):
    return {"status": "success", "message": msg}


def error_msg(msg):
    return {"status": "error", "message": msg}


def gen_agent_number(first_name, last_name):
    return first_name[:2].upper()+'-'+last_name[:2].upper()+'-'+str(randint(212451, 8961621))


def auth_login(username, password):
    q = Agent.objects.get(email=username)
    if q:
        return q.first_name
    else:
        return False


def check_if_email_exists(email):
    try:
        Agent.objects.get(email=email)
        return True
    except:
        return False


def authenticate_user(email, password):
    try:
        agent = Agent.objects.get(email=email)
        return sha512_crypt.verify(password, agent.password)
    except:
        return False


def compare_password(password, confirm_new_password):
    return True if password == confirm_new_password else False



