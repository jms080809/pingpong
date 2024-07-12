# 베이스 이미지를 윈도우 서버 코어로 지정
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# 환경 변수 설정
ENV PATH="C:\myapp:${PATH}"

# 작업 디렉토리 생성
WORKDIR C:/myapp

# 파일 복사
COPY . .

# 포트 개방
EXPOSE 80

# 컨테이너 시작 시 실행할 명령
CMD ["echo", "Hello from Windows Docker!"]
