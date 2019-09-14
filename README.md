# Monitor

Monitor the Temperature of Raspberry pi 3 and notify if temperature reaches high values. Currently the high value is set to 65°C

## Required

- Python 3.6 or newer
- re package
- os package
- urllib or urllib2

You can install python packages from the command line with

```

pip install package_name

Example

pip install urlib2

```

## Instructions for Settings

- from_address = Write the **email address** you want the email to be **sent from** ( example@gmail.com inside the quotes )
- to_address = Write the **email address** you want the email to be **sent to** (example@gmail.com inside the quotes)

> If you want to be sent to the same address you can put the same address to from_address and to_address
