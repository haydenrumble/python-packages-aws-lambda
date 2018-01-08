

from __future__ import print_function
import json, time
import numpy as np 
import pandas as pd
import scipy as sp
from scipy.stats import norm
from scipy.integrate import quad
import pymysql


def unihandler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    print()
    print("Testing numpy...")
    a = np.linspace(-np.pi, np.pi, 100)
    b = np.cos(a)
    c = np.ones(25)
    print("inner product", np.dot(c, c))
    print()
    print("Testing scipy...")
    phi = norm()
    value, error = quad(phi.pdf, -2, 2)
    print(value)
    print()      
    print("Testing pandas...")
    data = sp.randn(5, 2)
    dates = pd.date_range('28/12/2010', periods=5)
    df = pd.DataFrame(data, columns=('price', 'weight'), index=dates)
    result=df.mean()
    print(result)
    print()
    print("Testing PyMySQL...")
    print(dir(pymysql))
    print()
    print("Logging info:")
    print("Log stream name:", context.log_stream_name)
    print("Log group name:",  context.log_group_name)
    print()
    print("Context info:")
    print("Request ID:",context.aws_request_id)
    print("Mem. limits(MB):", context.memory_limit_in_mb)
    print("Time remaining (MS):", context.get_remaining_time_in_millis())
    return event['key1']

