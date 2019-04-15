#!/usr/bin/python
import sqlite3
import cgi
from urlparse import urlparse

print "Content-type: text/html\n\n"

def printTable(all_rows, headers):
  print "<table border='1'>"
  print "<tr>"
  for header in headers:
    print "<th>" + str(header) +"</th>"
  print "</tr>"
  for row in all_rows:
    print "<tr>"
    for col in row:
      print "<td>" + str(col) + "</td>"
    print "</tr>"
  print "</table>"

sqlite_file = "database/sample.db"
with sqlite3.connect(sqlite_file) as conn:
  c = conn.cursor()
  form = cgi.FieldStorage()
  if 'table' in form:
    table = form['table'].value
    c.execute('SELECT * FROM ' + table)
  elif 'sql' in form:
    table = 'Freeform SQL Query'
    sql = form['sql'].value
    sql = urlparse(sql).path
    print sql
    c.execute(sql)

  print "<br /><label><h3>" + table + "</h3></label>"
  headers = [desc[0] for desc in c.description]
  all_rows = c.fetchall()
  printTable(all_rows, headers)
