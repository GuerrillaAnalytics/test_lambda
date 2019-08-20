# -*- coding: utf-8 -*-
import os

def handler(event, context):
    # Your code goes here!
    e = event.get("e")
    pi = event.get("pi")
    result = my_logic(e, pi)
    return result


def my_logic(first_number, second_number):
    env_1 = os.environ['env_1']
    print(env_1)
    return first_number + second_number
