#!/usr/bin/env python3
import cgi
import cgitb

def main():

    cgitb.enable(display=0, logdir="/home/jacob/Code/HackNC2018/logs/")
    
    print("Content-Type: text/html")
    print()
    print("<!DOCTYPE html>")
    
    form = cgi.FieldStorage()
    if "name" not in form or "addr" not in form:
        print("<H1>Error</H1>")
        print("Please fill in the name and addr fields.")
        return
    print("<p>Name:", form["name"].value, "</p>")
    print("<p>Address:", form["addr"].value, '</p>')

main()
