# -*- coding: utf-8 -*-
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    # Your code goes here!
    logger.info(event)

    e = event.get("e")
    pi = event.get("pi")
    result = my_logic(e, pi)
    print("result= "+ result)
    return result


def my_logic(first_number, second_number):
    env_1 = os.environ["env_1"]
    print("env_1= " + env_1)
    return first_number + second_number
