# PyZenvia

[![Build Status](https://travis-ci.org/MrLucasCardoso/pyzenvia.svg?branch=master)](https://travis-ci.org/MrLucasCardoso/pyzenvia)  [![Code Health](https://landscape.io/github/mrlucascardoso/pyzenvia/master/landscape.svg?style=flat)](https://landscape.io/github/mrlucascardoso/pyzenvia/master) [![Coverage Status](https://coveralls.io/repos/github/MrLucasCardoso/pyzenvia/badge.svg?branch=master)](https://coveralls.io/github/MrLucasCardoso/pyzenvia?branch=master) [![PyPi Version](https://img.shields.io/badge/pypi-v0.4-blue)](https://pypi.org/project/PyZenvia/)

Package for send sms by Zenvia API

# Installation

## Prerequisites

- Python version >= 3.6
- Your account and password

```bash
$ pip install pyzenvia
```

# Usage

```python
from pyzenvia import Sender
sender = Sender(account, password)
response = sender.send(phone, message)
print(response['success'])
print(response['result'])
print(response['error'])
```

## Send SMS on command line

```
python -m pyzenvia --account zenvia_account_id --password mypass 5599999999999 "Sent using pyzenvia"
```
