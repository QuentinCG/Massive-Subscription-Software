# Massive-Subscription-Software
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/006d1d834eae4070a276cf80c1e51cf7)](https://www.codacy.com/manual/QuentinCG/Massive-Subscription-Software?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=QuentinCG/Massive-Subscription-Software&amp;utm_campaign=Badge_Grade)  [![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://github.com/QuentinCG/Massive-Subscription-Software/blob/master/LICENSE)

## What is it

This python software is designed to subscribe to numerous
newsletter or website at once.
It is multi-platform and compatible with python 2.7+ and 3+.

<img src="subscribe.jpg">

## How to install (python script and shell)

- Install Requests:
  - Solution 1: "pip install requests"
  - Solution 2: Download package at https://github.com/kennethreitz/requests and use "python setup.py install" command)
- Add all newsletter and website subscription in list_request.py (follow examples in the file)
- Load your shell or python script

## How to use in shell

```shell
# Get help
main.py -h

# Basic request
main.py --email example@example.com

# Full request
main.py --email example@example.com --pseudo johndoe --surname Doe --forename John --password Azerty1234 --postcode 12345 --day 10 --month 10 --year 1980
```

## License

This project is under MIT license. This means you can use it as you want (just don't delete the library header).

## Contribute

If you want to add more examples or improve the library, just create a pull request with proper commit message and right wrapping.
