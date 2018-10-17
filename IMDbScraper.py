#!/usr/bin/env python3

# Author: Akshay Shrimali (@marvin08)

import re
import mysql.connector
from mechanicalsoup import StatefulBrowser
from bs4 import BeautifulSoup
import datetime
import smtplib
from email.message import EmailMessage
from passlib.hash import cisco_type7

password = cisco_type7.decode("047B4F1718245E5A100C0C18022B48")

while(1):

  # Taking input from user.
  emailID = input("Email address: ")
  series = input("TV Series: ")

  db1 = mysql.connector.connect(host="127.0.0.1", user="yourUsername", passwd="yourPassword")
  cursor = db1.cursor()

  # Creating MySQL database - "projectDB".
  cursor.execute("CREATE DATABASE IF NOT EXISTS projectDB")

  db2 = mysql.connector.connect(host="127.0.0.1", user="yourUsername", passwd="yourPassword", database="projectDB")
  cursor2 = db2.cursor()

  # Creating MySQL table - "userData".
  cursor2.execute("CREATE TABLE IF NOT EXISTS userData (EmailID NVARCHAR(320), TV_Series VARCHAR(255))") 

  series1 = re.sub(r'\s', '', series).split(',')
  m = len(series1)
  sendmsg1 = [0] * m

  # Inserting into the table.
  sql = "INSERT INTO userData (EmailID, TV_Series) VALUES (%s, %s)"

  for x in range(m):
      values = (emailID, series1[x])
      cursor2.execute(sql, values)

  # Fetching data from the table.
  sql2 = "SELECT TV_Series FROM userData WHERE EmailID = %s"
  cursor2.execute(sql2, (emailID, ))
  entries = cursor2.fetchall()

  baseURL = 'http://www.imdb.com/find?q='

  for x in range(m):
      search = re.sub(r"\(", "", str(entries[x]))
      search2 = re.sub(r"\)", "", str(search))
      search3 = re.sub(r"\,", "", str(search2))
      search4 = re.sub(r"\'", "", str(search3))

      URL = baseURL + search4 + '&s=all'

      browse = StatefulBrowser()
      browse.open(URL)

      link = browse.find_link(url_regex = re.compile(r'/title/tt\d+/\?ref_=fn_al_tt_1'))
      res = browse.follow_link(link)

      link2 = browse.find_link(url_regex = re.compile(r'/title/tt\d+/episodes\?season=\d+&ref_=tt_eps_sn_\d+'))
      res2 = browse.follow_link(link2)

      soup1 = BeautifulSoup(res.text, "html.parser")
      soup2 = BeautifulSoup(res2.text, "html.parser")

      title = soup1.find("div", class_ = "title_wrapper")
      title1 = title.h1.text
      title2 = str(title1).rstrip()

      air_date = soup2.find_all("div", class_ = "airdate", text = re.compile(r'\d+\s\w+\.\s\d+'))

      if(air_date != []):
        t = re.sub(r'[\s+]', '', str(air_date[-1].text))
        t1 = re.sub(r'\\n', '', str(t))
        t2 = re.sub(r'\.', '', str(t1))
        
        presentDate = datetime.datetime.now()
        
        date2 = datetime.datetime.strptime(str(t2), "%d%b%Y")
        date3 = date2.strftime("%Y")
        
        if(int(presentDate.strftime("%Y")) == int(date2.strftime("%Y"))):
          if(int(presentDate.strftime("%m")) == int(date2.strftime("%m"))):
            if(int(presentDate.strftime("%d")) == int(date2.strftime("%d"))):
              s = "The show has finished seaming all its episodes."
            elif(int(presentDate.strftime("%d")) > int(date2.strftime("%d"))):
              j = 2
              while(int(presentDate.strftime("%d")) > int(date2.strftime("%d"))):
                i1 = len(air_date) - j
                t = re.sub(r'[\s+]', '', str(air_date[i1].text))
                t1 = re.sub(r'\\n', '', str(t))
                t2 = re.sub(r'\.', '', str(t1))
                date2 = datetime.datetime.strptime(s(t2), "%d%b%Y")
                if(int(presentDate.strftime("%d")) <= int(date2.strftime("%d"))):
                  t = re.sub(r'[\s+]', '', str(air_date[i1+1].text))
                  t1 = re.sub(r'\\n', '', str(t))
                  t2 = re.sub(r'\.', '', str(t1))
                  date2 = datetime.datetime.strptime(s(t2), "%d%b%Y")
                  s = "The next episode airs on " + date2.strftime("%Y-%m-%d") + "."
                  break
                j+=1
            elif(int(presentDate.strftime("%d")) < int(date2.strftime("%d"))):
              j = 2
              while(int(presentDate.strftime("%d")) < int(date2.strftime("%d"))):
                i1 = len(air_date) - j
                t = re.sub(r'[\s+]', '', str(air_date[i1].text))
                t1 = re.sub(r'\\n', '', str(t))
                t2 = re.sub(r'\.', '', str(t1))
                date2 = datetime.datetime.strptime(str(t2), "%d%b%Y")
                if(int(presentDate.strftime("%d")) >= int(date2.strftime("%d"))):
                  t = re.sub(r'[\s+]', '', str(air_date[i1+1].text))
                  t1 = re.sub(r'\\n', '', str(t))
                  t2 = re.sub(r'\.', '', str(t1))
                  date2 = datetime.datetime.strptime(str(t2), "%d%b%Y")
                  s = "The next episode airs on " + date2.strftime("%Y-%m-%d") + "."
                  break
                j+=1
          elif(int(presentDate.strftime("%m")) > int(date2.strftime("%m"))):
            s = "The show has finished seaming all its episodes."
          elif(int(presentDate.strftime("%m")) < int(date2.strftime("%m"))):
            j = 2
            while(int(presentDate.strftime("%m")) < int(date2.strftime("%m"))):
                i1 = len(air_date) - j
                t = re.sub(r'[\s+]', '', str(air_date[i1].text))
                t1 = re.sub(r'\\n', '', str(t))
                t2 = re.sub(r'\.', '', str(t1))
                date2 = datetime.datetime.strptime(str(t2), "%d%b%Y")
                if(int(presentDate.strftime("%m")) == int(date2.strftime("%m"))):
                  if(int(presentDate.strftime("%d")) >= int(date2.strftime("%d"))):
                    t = re.sub(r'[\s+]', '', str(air_date[i1].text))
                    t1 = re.sub(r'\\n', '', str(t))
                    t2 = re.sub(r'\.', '', str(t1))
                    date2 = datetime.datetime.strptime(str(t2), "%d%b%Y")
                    s = "The next episode airs on " + date2.strftime("%Y-%m-%d") + "."
                    break
                  if(int(presentDate.strftime("%d")) < int(date2.strftime("%d"))):
                    k = 1
                    while(int(presentDate.strftime("%d")) < int(date2.strftime("%d"))):
                      l = i1 - k
                      t = re.sub(r'[\s+]', '', str(air_date[l].text))
                      t1 = re.sub(r'\\n', '', str(t))
                      t2 = re.sub(r'\.', '', str(t1))
                      date2 = datetime.datetime.strptime(s(t2), "%d%b%Y")
                      if(int(presentDate.strftime("%d")) >= int(date2.strftime("%d"))):
                        t = re.sub(r'[\s+]', '', str(air_date[l+1].text))
                        t1 = re.sub(r'\\n', '', str(t))
                        t2 = re.sub(r'\.', '', str(t1))
                        date2 = datetime.datetime.strptime(str(t2), "%d%b%Y")
                        s = "The next episode airs on " + date2.strftime("%Y-%m-%d") + "."
                        break
                      k+=1
                j+=1
        elif(int(presentDate.strftime("%Y")) > int(date2.strftime("%Y"))):
            s = "The show has finished seaming all its episodes."
        elif(int(presentDate.strftime("%Y")) < int(date2.strftime("%Y"))):
            s = "The next season begins in " + s(date3) + "."

        s2 = "\nTv series name: " + str(title2)
        s3 = "\nStatus: " + s
        sendmsg = s2 + s3
        sendmsg1[x] = sendmsg

      else:
        air_date = soup2.find_all("div", class_ = "airdate", text = re.compile(r'\d+'))
        
        t = re.sub(r'[\s+]', '', str(air_date[-1].text))
        t2 = re.sub(r'\\n', '', str(t))
        
        presentDate = datetime.datetime.now()

        date2 = datetime.datetime.strptime(str(t2), "%Y")
        date3 = date2.strftime("%Y")

        presentDate = datetime.datetime.now()
        
        s = "The next season begins in " + str(date3) + "."
        s2 = "\nTv series name: " + str(title2)
        s3 = "\nStatus: " + s
        sendmsg = s2 + s3
        sendmsg1[x] = sendmsg
        
  sendmsg2 = "\n".join(sendmsg1)

  sendmsg3 = EmailMessage()
  sendmsg3["Subject"] = "Updates about the " + str(m) + " TV Series you asked for!"
  sendmsg3["From"] = "musicalcoder17@gmail.com"
  sendmsg3["To"] = emailID
  sendmsg3.set_content(sendmsg2)

  # Creating and starting the SMTP server to send the e-mail.
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("musicalcoder17@gmail.com", password)
  server.send_message(sendmsg3)
  server.quit()
  
  print("\n")
