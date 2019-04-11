#!/usr/bin/python
import sqlite3

print "Content-type: text/html\n\n"

def printItems(all_items):
    for item in all_items:
        print "<option value='"+item[0]+"'>"+item[0]+"</option>"

sqlite_file = "database/sample.db"
with sqlite3.connect(sqlite_file) as conn:
  c = conn.cursor()
  c.execute("select name FROM sqlite_master WHERE type='table';")
  all_items = c.fetchall()

  print "<select id='dbtable' name='dbtable'>"
  print "<option>select table</option>"
  printItems(all_items)
  print "</select>"
