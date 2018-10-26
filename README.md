# daiski-bot

10분에 한번씩 [2018 열과 통계물리 게시판](http://phya.snu.ac.kr/php/subject_list/Notice/list.php?id=2018_tsp)의
새 글을 확인하여 슬랙에 알림 메시지를 보내줍니다.

사용 방법:
- `secret.txt`에 슬랙 API webhook 주소를 넣는다.
	- 예시: `https://hooks.slack.com/services/********/********/**********************`
- `python bot.py`
