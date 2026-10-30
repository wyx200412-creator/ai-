# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:30:15 2026

@author: 86132
"""

import requests

data = Task(
    title: "学习 Pydantic",
    done: False
)

response = requests.post(
    "http://127.0.0.1:8000/tasks",json=data
)

print(response.status_code)
print(response.json())