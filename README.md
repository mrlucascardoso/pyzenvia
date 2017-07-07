# PyZenvia

[![Build Status](https://travis-ci.org/MrLucasCardoso/pyzenvia.svg?branch=master)](https://travis-ci.org/MrLucasCardoso/pyzenvia)  [![Code Health](https://landscape.io/github/MrLucasCardoso/pyzenvia/master/landscape.svg?style=flat)](https://landscape.io/github/MrLucasCardoso/pyzenvia/master) [![Coverage Status](https://coveralls.io/repos/github/MrLucasCardoso/pyzenvia/badge.svg?branch=master)](https://coveralls.io/github/MrLucasCardoso/pyzenvia?branch=master)

Package for send sms by Zenvia API

To use it is necessary to set two environment variables, one for the authentication key of Zenvia and another to set BASE_URL. The BASE_URL must be set because you can test the messages in a Zenvia test url

# Installation

## Prerequisites

- Python version 3.4, 3.5 or 3.6
- Environment variables
    - ZENVIA_TOKEN=your token
    - ZENVIA_URL=test zenvia url

```bash
$ pip install pyzenvia
```

# Usage

```python
from pyzenvia import Sender
sender = Sender('5586912344321', 'Hello')
response = sender.send()
print(response['success'])
print(response['results'])
```
