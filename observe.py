#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8') 

import urllib2
import datetime
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from bs4 import BeautifulSoup

def observe():
	page = urllib2.urlopen('http://www.bjjs.gov.cn/bjjs/xxgk/ztzl/gycqzf/index.shtml').read()
	soup = BeautifulSoup(page)
	# newsResult = soup.findAll('span', attrs = {"class" : "left"})
	ul = soup.find('ul', attrs = {"class" : "ul_list"})
	first_li_span = ul.li.span
	latest_date_str = first_li_span.contents[0]
	latest_date = datetime.datetime.strptime(latest_date_str, "%Y-%m-%d")
	last_date = datetime.datetime.strptime("2017-09-30", "%Y-%m-%d")
	print(latest_date)
	print(last_date)
	return latest_date > last_date


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))


def send(title, content, to_addr):
	from_addr = 'caoyuznb@163.com'
	password = 'cy19920927'
	smtp_server = 'smtp.163.com'

	msg = MIMEText(content, 'plain', 'utf-8')
	msg['From'] = _format_addr('我 <%s>' % from_addr)
	msg['To'] = _format_addr('我 <%s>' % to_addr)
	msg['Subject'] = Header(title, 'utf-8').encode()

	server = smtplib.SMTP(smtp_server)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()


if observe():
	send('新提醒！', '共有资产房有新消息！', 'caoyuznb@163.com')
	send('新提醒！', '共有资产房有新消息！', '1256818321@qq.com')


