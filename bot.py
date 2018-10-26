import requests
import os
import re
import time

subject = '2018_tsp'
url = 'http://phya.snu.ac.kr/php/subject_list/Notice/list.php?id={subject}'
webhook_url = ''
post_url = 'http://phya.snu.ac.kr/php/subject_list/Notice/view.php?id={subject}&uid={postid}'
headers = {
    'Content-type': 'application/json',
}

def get_postlist():
	req = requests.get(url.format(subject=subject))
	html = req.text.replace('\n', '').replace('\r', '')
	arr = re.findall(r'page=1&uid=(.*?)</a>', html)
	ret = []
	for post in arr:
		postid, title = post.split('&keyfield=&key=">')
		ret.append((postid, title))
	return ret

def load_postlist():
	try:
		with open('list.txt', 'r') as f:
			return f.readline().strip().split(',')
	except FileNotFoundError:
		return []

def save_postlist(postlist):
	with open('list.txt', 'w') as f:
		f.write(','.join(postlist))

def initialize_bot():
	global webhook_url
	with open('secret.txt', 'r') as f:
		webhook_url = f.readline().strip()

def format_message(post):
	postid, title = post
	link = post_url.format(subject=subject, postid=postid)
	return title + '\n' + link

def send_message(message):
	data = '{"text":"' + message + '"}'
	resp = requests.post(webhook_url, headers=headers, data=data.encode('utf-8'))

if __name__ == '__main__':
	initialize_bot()
	while True:
		update = False
		new_postlist = get_postlist()
		old_postlist = load_postlist()
		for x in new_postlist:
			if x[0] not in old_postlist:
				update = True
				print('Found new post - %s' % time.strftime('%y/%m/%d %H:%M:%S'))
				send_message(format_message(x))

		if update:
			save_postlist(new_postlist)
		
		time.sleep(600) # check every 10 min.
