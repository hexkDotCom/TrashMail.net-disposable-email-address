Import disposable emails from SpamGourmet service.
======================================
The script is based on the work of - Laszlo Szathmary, 2013 (<jabba.laci@gmail.com>), <https://github.com/jabbalaci/TrashMail.net-disposable-email-address>

Creates a disposable email address on TrashMail.net (<https://ssl.trashmail.net/>).

First, you must register yourself on trashmail.net (it's free). With these
credentials you can access the address manager of TrashMail.net. Emails will be
redirected to the address that you set upon registration.

Then, you must provide your credentials to this script. Either you
hard-code it in the source (USERNAME and PASSWORD variables), or
you provide them interactively.

The script takes a list of disposable email address from a text file and 
adds them for you on TrashMail.net.

Tested under Windows 10 with Python 2.7.

Usage
-----

    ./trashmail.py

Sample output:

    # copied to the clipboard
    prcb107f@trashmail.net
