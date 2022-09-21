jenkins 컨테이너 안에서 git으로 받은거 빌드 한 다음에(gradlew 권한 설정 해줘야함) host로 와서 볼륨으로 동기화된 폴더 들어가서 jar 파일을 이미지 빌드하고 컨테이너 올릴려고 docker-compose 실행

jenkins 컨테이너에서 host로 접속하기 위해 ssh 설정을 해주어야함



```shell

pwd
cd /var/jenkins_home/workspace/recipeNav/BE/recipenav/
echo "gradle start"
chmod 777 ./gradlew
./gradlew build

ssh -t -t ubuntu@host.docker.internal<<EOF
 cd /jenkins/workspace/recipeNav/BE/recipenav
 docker build -t spring-image .
 cd /home/ubuntu/spring_compose_folder
 docker-compose up --build -d
 exit
EOF
```


