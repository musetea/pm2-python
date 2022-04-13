# PM2로 파이썬 스크립트 관리

## 목적 
- 파이썬 스크립트 관리 
- __PM2__(NodeJS) 인 모듈 관리 시스템으로 파이썬 스크립트를 관리
- 리눅스에서 _Crontab_을 사용할경우 관리/로깅할 작업많고 어려움


## 체크사항 
-- 하나의 파이썬 프로그램을 파이썬의 여러 가상환경에서 구동 및 관리되는지?
-- PM2 사용방법
-  PM2 클러스터
    - 사용은 가능하나 `Node.js 는 클러스터를 지원해서 PORT 포트를 공유하는 하위프로세스를 생성해서 지원함`. 
    - FastApi 을 지원하는 uvicorn 에서는 사용 할 수 없음.

- uvicorn 자체에  `workers`수 를 지원함. 
    - 단일 프로세스로 비동기 처리


### PM2
- 자동로드가능 [watch]
- 스캐줄러 기능 [cron]
- 모든 프로그램 관리 가능
```sh
    npm install pm2@latest -g
    npm install -g npm@8.6.0
    # 원도우 [정책권한]
    $ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

## 스크립트 자동화
- .py 파일을 시작할때 파이썬 스크립트를 실행함.
- 기본적으로 __자동 재실행__ 함 
- 환경설정파일 (`ecosystem.config.js`) : 파일명이 고정인듯함, 다른 파일명으로 하면 동작안함.
```sh
    `--interpreter` python3                 # 파이썬 버전선택
    `--restart-delay` <xxxx ms>             # 재부팅 후 지연 실행
    `-10s-delay`                            # 10초 지연실행
    `--cron '*/1 * * * *' `     #  UNIXOS시간기반<분 시 월 달 주> , 1분마다실행
    `--no-autorestart`          # 자동재시작 막음


```
- 콘솔에서 5분마다 재실행 
- pm2 start src\main.py --name job39 --interpreter venv39\Scripts\python.exe --cron "*/5 * * * *" --no-autorestart
- pm2 start src\main.py --name job310 --interpreter venv310\Scripts\python.exe --cron "*/5 * * * *" --no-autorestart

- pm2 start ecosystem.config.js # 설정파일로 실행하기

### PM2 명령어
```sh
`--watch` : # 디렉토리/하위디렉토리 에서 변경있을경우 자동  재시작
`--watch:["src"]` :          #폴더 지정
`--ignore_watch` : ["node_modules"] :     #폴더 제외
`--attach` : # 앱실행 후 로그출력.

`start` # 시작
`stop`  # 정지
`delete`    # 삭제
`restart`   # 재시작
`list`  # 프로세스 목록

```



## 참고
[PM2](https://github.com/Unitech/pm2)  
[PM2 - 블로그](https://towardsdatascience.com/automate-your-python-script-with-pm2-463238ea0b65)
[UVICORN 성능문제](https://breezymind.com/uvicorn-0-16-0-performance-problem/)
[GUNICORN](https://jonnung.dev/python/2021/10/24/asgi-uvicorn-with-guicorn/)
