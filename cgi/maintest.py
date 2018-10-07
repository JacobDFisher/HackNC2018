#!/usr/bin/env python3
import cgi
import cgitb

def main():

    cgitb.enable(display=0, logdir="/home/jacob/Code/HackNC2018/logs/")

    print("Content-Type: text/html")
    print()
    print("<!DOCTYPE html>")
    print("<title>Welcome, valued customer</title>")

    print('<form action = "/cgi-bin/pythoncgitest.py" method = "post" target="test_iframe">\n\tName: <input type = "text" name = "name" /><br />\n\tAddress:<input type = "text" name = "addr" />\n\t<input type = "submit" value = "Submit" />\n\t</form>')
    print('<iframe name="test_iframe" src="/cgi-bin/pythoncgitest.py"></iframe>')

main()
