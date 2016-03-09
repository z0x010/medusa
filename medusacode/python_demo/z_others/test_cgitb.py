#!/usr/bin/env python
# coding:utf-8

"""
Traceback manager for CGI scripts

The cgitb module provides a special exception handler for Python scripts.
(Its name is a bit misleading. It was originally designed to display extensive traceback information in HTML
for CGI scripts. It was later generalized to also display this information in plain text.)
After this module is activated, if an uncaught exception occurs, a detailed, formatted report will be displayed.
The report includes a traceback showing excerpts of the source code for each level,
as well as the values of the arguments and local variables to currently running functions,
to help you debug the problem. Optionally, you can save this information to a file instead of sending it to the browser.
"""

import cgitb

cgitb.enable(format='text')

print 1/0
