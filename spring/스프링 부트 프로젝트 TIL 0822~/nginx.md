# Nginx 란

Apache와 같은 웹서버

클라이언트로부터 요청이 들어오면 요청에 맞는 처리를 한다

또한 Reverse Proxy Server를 활용하여 WAS의 부하를 줄일 수 있는 로드 밸런서로 활용

- Reverse Proxy Server : 외부 클라이언트에서 서버로 접근 시, 중간에서 중개자 역할을 하며 외부로부터 내부망에 있는 서버의 존재를 숨길 수 있다.

- 로드 밸런서 : 
  
  - 서버의 부하를 분산해주는 역할을 하는 장치 또는 소프트웨어
  
  - 기본적으로 Reverse Proxy를 기반으로 동작한다
  
  - Reverse Proxy Server가 내부 서버에 대한 정보를 알고 있으므로 각 서버의 상태에 따라 부하를 분산시키며 요청을 전달할 수 있다

# 사용법

1. Nginx는 기본적으로 설정파일의 지시어에 따라 동작

2. AWS EC2 서버에 Nginx를 설치하게 되면 기본 설정파일들(ex. /etc/nginx/nginx.conf)이 생성, 해당 파일에서는 http 요청에 대한 설정과 Nginx가 사용할 프로세스 수 등을 지시어를 사용하여 설정

3. 지시어 : 단위로 이루어진 simple 지시어와 simple 지시어를 블록 {}으로 감싼 block 지시어
   
   1. Block 지시어 : nginx의 block 지시어인 http, server, location 블록은 계층 구조를 가지고 있다. http 블록의 내용은 server 블록의 기본값이 되고 server 블록의 내용은 location 블로그이 기본값이 된다
      
      1. http 블록 : HTTP 부분과 관련된 모듈의 지시어와 블록을 정의, server블로고가 location의 루트 블록
      
      2. server 블록 : 하나의 호스트를 선언하는데 사용, http 블록 안에서만 사용할 수 있고 한 개 이상의 location 블록을 선언할 수 있다
      
      3. location 블록 : server 블록 안에 정의되며 특정 URL을 처리하는 방법을 정의
      
      ```shell
      http {
          server {
          listen 80;    // 80번 포트로 요청을 받는다    
      
          location / {        //도메인:80로 요청이 들어왔다면 /path/to/html에서 응답할 파일을 찾는다
              root /path/to/html ;
          }
      
          location /test/ {        //도메인:80/test로 요청이 들어왔다면 /path/to/test에서 응답할 파일을 찾는
              root /path/to/test;
          }
      }
      }
      ```

                  - listen : http 요청을 받는 IP주소와 포트를 설정한다

                  - root : 응답할 파일이 위치한 문서의 루트를 정의한다

4. Reverse Proxy Server 설정
   
   ```shell
   http {
       sever {
           listen 80;
           location / {
               proxy_pass http://127.0.0.1:8080;
           }
           location /test {
               proxy_pass http://127.0.0.1:8080/test;
           }
       }
   }
   ```
   
   - listen에 지정된 포트(default: 80)로 요청이 들어오면 location/에 해당되고 이 요청은 proxy 서버에 의해 http://127.0.0.1:8080로 포워딩한다
   
   - ~:80/test로 요청이 들어오면 location /test에 해당되고 이 요청은 proxy 서버에 의해 http://127.0.0.1:8080/test 로 포워딩 한다
