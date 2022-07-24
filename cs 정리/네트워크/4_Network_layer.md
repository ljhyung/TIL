# Network layer 1

>  Introduction, Virtual circuit and datagram, networks

## 네트워크 계층의 소개

- 네트워크 계층의 목적
  - Host to Host 간의 통신을 담당한다.
  - Transport 계층에서 담당했던 Process to Process가 두 소프트웨어 사이의 통신이라면 Host to Host 통신은 물리적인 실체인 Host (PC나 라우터 등) 간의 통신이다.
  - Transport 계층과의 차이
    - Host 간 전송
    - Application에게 선택권한 없음
    - 코어에서 구현된다.
- 호스트와 라우터의 차이
  - 라우터는 컴퓨터 네트워크간 데이터 패킷을 알맞은 경로로 보내는 네트워크 장치이다.
  - 일반적인 호스트와 라우터 둘 다 네트워크 계층이 있지만 라우터의 라우팅 테이블이 훨씬 더 방대하며 호스트는 자신의 게이트웨이 라우터의 주소만 알고 있다.
- 네트워크 계층의 기능
  - 라우팅 : 해당 목적지로 가는 적절한 경로를 계산한다.
  - 포워딩 : Input 포트로 들어온 데이터그램을 적절한 output 포트로 내보낸다.
- 네트워크 서비스 모델
  - 한 패킷에 대해 (미시적 관점)
    - datagram의 전송을 보장한다.
    - minimum delay를 보장한다.
  - 여러 패킷에 대해 (거시적 관점)
    - In-Order를 보장한다.
    - Minimum Bandwidth를 보장한다.
    - 최소한의 패킷간 시간차를 보장한다.
- 패킷 스위칭의 두가지 방법
  - Virtual Circuit : Connection Oriented
  - Datagram : Connection Less

- Virtual Circuit
  - 네트워크 장비간 (라우터간) 데이터 전송 전 콜 셋업으로 경로를 미리 설정하고
  - 각 패킷은 VCID를 가지고 있다.
  - 라우터는 VC State를 가지고 있다.
  - VCID는 라우터를 지날 때마다 변한다. ( 지나치는 모든 라우터들에 대해 동일한 ID를 유지할려면 큰 비트가 필요하기 때문)
    - 라우터들은 각 VC에 대해 forwarding table을 가지고 있다.
  - 네트워크 코어가 복잡해지므로 인터넷엔 맞지 않고
  - Smart한 Endsystem보다 Dumb한 Endsystem에 어울린다.(전화 등)
- Datagram Network
  - 커넥션을 맺지 않으므로 경로설정이 없다.
  - 라우터는 Stateless하게 전달만 한다.
  - 패킷은 패킷 헤더에 있는 목적지 주소에 의해서만 포워딩된다.
  - 하지만 모든 목적지 주소에 대해 포워딩 테이블을 만드는 것을 굉장히 비효율적이므로
  - Address Range ( IP Prefix)에 따라 어느 output 링크로 보낼 건지 결정한다.



# Network layer 2

>  what’s inside a router, IP: Internet Protocol

## 라우터 아키텍처

- 라우터는 Control Plane과 Data Plane으로 구성된다.
  - Control Plane
    - 라우터의 두뇌 부분에 해당한다.
    - Control Plane의 프로세서가 라우팅 알고리즘을 실행하고 포워딩 테이블을 업데이트한다.
    - 포워딩 테이블 :  Input으로 들어온 패킷을 어떤 Output Port로 보낼지 적혀있는 테이블이다.
    - 소프트웨어적이다.
  - Data Plane
    - 빠른 속도를 위해 하드웨어적으로 구현되어 있다.
    - 데이터 전송을 담당한다.
    - Input Port, Switching Fabric, Output Port로 구성되어 있다.



![img](https://blog.kakaocdn.net/dn/buIvpH/btqGqaCGrGb/BNyZdMxXkT7gEXlIXMyBQ1/img.png)



------

## Input Port

- 하위계층 레이어인 Physical Layer ( Line Termination)과 Link Layer protocol 도 포함되어 있다.
  - 각각은 비트 신호를 프레임으로 생성하고, 한 링크를 잘 건너왔는지 분석한다.
- Look Up, Forwading, Queueing
  - Datagram의 헤더 필드의 목적지와 Input port 메모리의 포워딩 테이블(이건 Control Plane이 업데이트한다.)을 봐서 어디로 갈지 (Output Link)를 결정하고 버퍼에 넣는다. (Queueing).
  - 왜 버퍼에 넣을까?
    - Switching Fabric에 들어가기를 기다린다.
    - 여담으로 네트워크 얘기를 하다 보면 자꾸 버퍼가 나온다. 여러 시스템이 연결된 아키텍처에서는 시스템 간 파이프라이닝을 위해 버퍼가 필요하다는 것을 알 수 있다.
- Input 포트에서 하는 일을 요약하자면
  - 링크를 건너온 데이터그램을 받아서 포워딩 테이블을 봐서 어디로 갈지 결정하고 대기시킨다.

 

------

## Switching Fabric

- Switch 한다는 건 무엇일까?
  - 맨 처음에 ISP 얘기를 할 때 모두가 모두에 대해 연결한다면 매우 비효율적이라고 했다.
  - 네트워크들 사이에 ISP ( 라우터라고 생각하자)를 둠으로써 각 호스트들은 ISP에만 연결하면 다른 호스트들과 연결할 수 있었다.
  - 여기서 ISP가 스위칭한다고 한다.
- Switching Fabric이란?
  - 여러 개의 Input Port와 Output Port들을 스위칭하는 패브릭이다.
  - 패브릭은 비유적인 표현이고 그냥 복잡한 회로 뭉태기라고 생각하자.
- Head of Line Blocking
  - 스위칭 패브릭에 Input Port들에서 데이터가 들어오는 속도가 스위칭하는 속도보다 느리면 Input Port의 큐에 쌓인다.
  - 한 Output Port에는 동시에 하나의 데이터그램만 지날 수 있으므로 같은 Output Port로 나가려 하는 두 Datagram이 동시에 Switching Fabric에 들어오는 경우 Output Port Contention이 생긴다. 이 경우 Contetion으로 인해 기다리는 데이터그램 뒤에 Contention이 없는 데이터그램은 Contetion이 없는데도 기다리게 된다.
- Switching Fabric의 종류
  - Memory : CPU의 컨트롤을 직접적으로 받고 시스템 버스를 두 번 타야 하므로 느리다. 초기에 사용되었음
  - Bus : Single Bus는 Bus Contention이 쉽게 발생한다.
  - Interconnection : 여러 개의 버스를 교차해서 Bandwidth를 극복한다.
    - 하드웨어의 처리속도를 높이기 위해 데이터그램을 Fixed Lengh Cell로 분할해서 속도를 높일 수 있다.

------

## Output Port

- 마찬가지로 Link에 실어 보내기 위해 버퍼가 필요하다.
- datagram buffer(network) - link layer protocol(send)(Link) - line termination(Physical)
- 어느 것을 먼저 내보낼지 큐 스케줄링이 필요하다.
  - 인터넷은 FCFS를 사용하나 다른 네트워크에선 우선순위 등을 사용할 수도 있음

------

## 라우터의 버퍼의 크기는 어떻게 해야 할까?

- 버퍼의 크기는 네트워크 패킷 흐름의 유동성에 비례해야 한다.
- 따라서 RTT * LinkCapacity를 생각할 수 있겠다.
- 통계적으로 Smooth 해질 수 있기 때문에 (CLT를 생각하자!) root(호스트의 수)로 나눠도 된다.

------

## IP : Internet Protocol

- 말 그대로 인터넷 상에서 통신을 위한 프로토콜이다.
- 네트워크 레이어에는 세 가지 프로토콜이 있다.
  - 라우팅 프로토콜 : RIP, OSPF, BGP
    - 경로 계산 데이터를 주고받는다
    - 즉 Control Plane과 관련이 있다.
    - 나중에 하나씩 살펴보자!
  - ICMP : Internet Control Message Protocol의 약자이다.
    - 에러 리포팅, 컨트롤 메시지 교환 등을 한다.
  - IP  : Internet Protocol
    - 주소, 데이터그램 형식, 패킷 핸들링을 담당한다.
    - Data Plane과 관련이 있다.

 

------

## IP 헤더



![img](https://blog.kakaocdn.net/dn/AQaM0/btqGvat3mnY/1dB10Jas7Vd4okrkrMWi6K/img.png)



- 프로토콜을 살펴볼 때 헤더를 보면 그 프로토콜이 무슨 기능을 하는지 알 수 있다.
- 하나씩 살펴보자
  - TCP와 마찬가지로 20바이트 + a로 구성된다.
  - ver : IPv4인지 v6인지 아이피 버전을 나타낸다.
  - head len : 헤더의 길이를 4바이트 단위로 나타낸다.
  - type of service : IP 패킷의 우선순위를 정한다.
  - length : 헤더 + 데이터의 길이를 나타낸다.
  - 16 bit id : 패킷의 ID로, 패킷이 분할되었을 때 재조립을 위해 사용된다.
  - flgs : 패킷이 단편화되었는지 / 단편의 마지막인지 나타낸다.
    - 세 비트로 구성
    - 첫 번째비트는 0
    - 두 번째비트는 단편화 유무에따라 1/0
    - 세 번째 비트는 더 있는지 유무에 따라 1/0
    - 단편화되어있고 자신이 마지막이면 010이다.
  - fragment offset : 패킷 조립 시에 offset에 8을 곱한 값이 시작 위치가 된다.(300인 경우 2400부터)
  - Time to live
    - 처음에는 임의로 정해진 TTL값으로 시작해서(윈도우 : 128, 리눅스 : 64) 한 홉 당 1씩 감소한다.
    - 0이 되면 패킷은 버려지고 ICMP로 송신자에게 알린다.
    - 네트워크를 떠도는 패킷이 없도록 한다.
  - Upper Layer : 상위 계층이 TCP인지 UDP인지 ICMP인지 알려준다.

------

## IP 단편화와 재조립 ( Fragmentation, Reassembly )

- MTU : Maximum Transmission Unit
  - 링크를 지날 수 있는 Frame의 최대 크기이다.
  - 인터넷은 다양한 링크들로 구성되어 있으므로 각자 다른 MTU를 가진다.
- IP 패킷이 링크를 지날 때 그 링크의 MTU보다 크면 독립적인 Datagram으로 분할된다.
- 네트워크 코어의 복잡성을 줄이기 위해서 단편화가 일어나는 것은 어쩔 수 없지만 재조립은 최종 목적지에서 하게 된다.
- 4000 바이트 길이의 데이터그램이 1500 MTU의 링크를 지나면서 3개로 분할되는 과정을 살펴보자.

| Length        | ID   | Fragemetation Flag | Offset |
| ------------- | ---- | ------------------ | ------ |
| 4000          | x    | 000                | 0      |
| 1500(1480+20) | x    | 011                | 0      |
| 1500(1480+20) | x    | 011                | 185    |
| 1040          | x    | 010                | 370    |

- 4000 byte 길이의 데이터그램은 헤더 20 byte + 데이터 3980 바이트이다.
- 첫번째 단편화된 데이터그램은 0~1480바이트의 데이터를 나타낸다.
- 두번째 단편화된 데이터그램은 1480~2960바이트의 데이터를 나타내므로 offset은 1480 / 8 = 185
- 세번째 단편화된 데이터그램은 2960~3980바이트의 데이터를 나타내므로 offset은 2960 / 8 = 370
- offset -> 8byte 당 1

 

------

## IP Addressing

- IP란?
  - IP는 네트워크 인터페이스의 주소이다.
  - IP는 서브넷 주소 + 호스트의 주소로 이루어져 있다.
- Subnet (서브넷) 이란?
  - 라우터의 개입 없이 통신할 수 있는 네트워크이다.
- CIDR : Classless Inter Domain Routing
  -  클래스에 따라 Subnet Portion이 정해진다. Subnet Portion이 작으면 더 많은 호스트를 수용할 수 있으므로
  - 대형 기관에 적합하다.
  - IP주소에 클래스를 별로 호스트 수를 정하면 낭비가 IP 주소 낭비가 심하다.
  - 클래스 없이 Subnet Portion을 가변적으로 정하자.



# Network layer 3

>   IP: Internet Protocol

## IP 주소 할당

- 할당 방법에는 두 가지 방법이 있다.
  - 시스템 파일에다 직접 입력하기
  - DHCP를 사용
    - Dynamic Host Configuration Protocol
    - 애플리케이션 계층의 프로로콜이다.
    - 동적으로 IP주소를 할당받는다.

 

------

## DHCP

- DHCP의 작동방식과 특징
  - IP를 동적으로 할당해주는 DHCP 서버를 브로드캐스팅 도메인 내에 둔다.
  - 호스트와 DHCP는 서로 브로드캐스팅을 통해 통신할 수 있다.
  - 호스트가 네트워크에 접속해있는 시간동안만 IP주소를 할당(임대)받는다.
  - 따라서 주소 재사용이 가능해서 IP주소를 효율적으로 사용할 수 있다.
  - IP 주소를 수동으로 설정할 필요 없이 Plug and play가 가능하다.
  - 포트번호는 67이다. 일회성 질의이므로 UDP를 사용한다.
- 네 개의 메세지로 구성된다.
  - DHCP discover
    - 호스트가 DHCP 서버를 찾기 위한 메세지이다.
    - 동일 서브넷 내에 브로드캐스팅된다.
    - 호스트의 맥 주소가 담긴다.
  - DHCP offer 
    - 유니캐스트나 브로드캐스트일 수 있다.
    - DHCP 서버가 호스트에게 자신의 존재를 알린다.
    - 할당 '될' IP 주소와 Local DNS 서버 주소, Subnet Portion, 이 메세지를 보낸 DHCP 서버의 주소, 게이트웨이 라우터 주소를 알려준다.
  - DHCP request
    - 브로드캐스트로 보낸다. 
    - 호스트는 DHCP 서버를 선택하고 해당 서버에게 호스트가 사용할 네트워크 정보를 정식으로 요청한다.
    - 호스트의 맥 주소, 호스트가 사용할 IP, DHCP 서버의 IP가 들어간다.
  - DHCP Ack
    - 브로드캐스트나 유니캐스트일 수 있다
    - DHCP offer 메세지와 동일한 정보를 제공해준다.
    - 정식으로 서버가 주소를 할당해준다.
  - discover 메세지와 offer 메세지는 optional이다.
- DHCP 서버의 추가적인 역할
  - 게이트웨이 라우터(First Hop 라우터)의 주소를 알려준다.
  - Local DNS 서버의 주소를 알려준다.
  - Network Mask(Subnet Portion, 32비트 주소중 어디까지가 Subnet을 가리키는 주소인지)

------

## 서브넷 주소할당

- 서브넷은 ISP로부터 주소블록을 할당받는다.
  - 예를들어서 ISP가 200.23.16.0 /20 주소블록을 가지고 있으면
  - 서브넷1은 200.23.16.0/23
  - 서브넷2는 200.23.18.0/23
  - ......
  - 마지막은 200.23.30.0/23
  - 이런 식이다. 이진수로 나타내서 생각해보면 이해가 된다.
  - **IP prefix**에 따라 계층적으로 주소할당이 된다.
- 계층적인 주소할당
  - 라우터에서 포워딩테이블을 탐색할 때 Input으로 들어온 패킷은 가장 Specific (Longest Prefix Match, 200.23.16.0/20 보다 200.23.18.0/23을 향해)한 주소를 가지는 Output 포트로 나간다.
  - **LPM**
- ISP가 보유하는 주소블록은 인터넷진흥원이 관리한다.

 

------

## NAT

- Network Address Translation의 약자이다.
- IP주소 고갈 문제
  - IPv4는 32비트 주소를 사용하므로 약 42억개의 주소를 할당할 수 있다.
  - 하지만 이마저도 점점 고갈되어간다.
- NAT란?
  - NAT는 하나의 Public IP를 서브넷 내에서만 사용할 수 있는 여러개의 사설 IP로 변환하는 시스템이다.
  - 게이트웨이 라우터만 Public IP를 가지고 있고 로컬 호스트들은 사설 IP를 가진다.
  - 서브넷 내의 호스트들은 포트번호로 구분된다.
  - 포트 포워딩
    - 라우터에서 [Public IP, Port번호]가 [Private IP, 호스트 내 포트번호]로 변환된다.
    - 예를 들어 한 호스트 내 프로세스가  [10.0.0.1, 3345]로 식별된다고 생각해보자.
      - 라우터는 [자신의 Public IP, 비어있는 포트번호]로 바꾸고 이를 자신의 테이블에 적는다.
      - 응답이 돌아오면 포트번호를 보고 어떤 호스트의 어던 프로세스인지 식별할 수 있다.
      - 즉 게이트웨이 라우터의 포트번호와 호스트의 프로세스를 매칭하는 원리다. 
- 관리상의 이점
  - LAN내의 모든 디바이스는 하나의 아이피만 있으면 된다.
  - 접속하는 ISP가 변해도 로컬 네트워크의 IP를 변경하지 않아도 된다.
  - 로컬 네트워크 내의 IP주소를 바꿀 때 외부에 알리지 않아도 된다.
  - 보안상의 이점이 있다.
- NAT의 문제점
  - end to end 통신을 침범한다.
  - NAT Traversal Problem
    - NAT로 구성된 LAN 내부에 서버가 있을 경우 Public IP만으로는 서버를 식별할 수 없다.
    - 그러므로 NAT 라우터는 정적으로 특정 포트를 서버에 할당한다.
- UPnP
  - Internet Gateway Device 프로토콜을 이용해서 자동으로 연결할 수 있다.



# Network layer 4

>  IP: Internet Protocol, Routing algorithms

## ICMP

- Internet Contorl Message Protocol의 약자이다.
  - IP 제어를 위해 사용되는 프로토콜이다.
  - 오류 보고, echo reply/ request 를 담당한다.
- ICMP는 IP 데이터그램에 캡슐화된다.
  - IP 패킷 페이로드 부분에 실린다.
  - ICMP는 직접 전송을 담당하는 프로토콜이 아니기 때문이다.
- Type과 Code, 오류를 일으킨 IP 데이터그램의 첫번째 8바이트로 구성된다.
  - Type과 Code
    - 0   0   Echo Reply (pong)
    - 3   3   목적지 포트 도착불가(Dest. port unreachable)
    - 11  0   TTL Expired
    - 8   0   Echo Request
    - Echo (에코, 반향)란? 에코는 수신측이 활성상태인지 확인하는 메세지이다.
  - TTL 과 포트 도착불가를 사용해서 어느 라우터들을 거쳐갔는지 알 수 있다.
    - ICMP 메세지에는 어느 라우터가 보냈는지가 담겨있기 때문이다.
    - 포트를 모르니깐 아무 포트나 보내서 경로를 탐색

 

------

## IPv6

- IPv4의 문제점
  - IPv4는 32비트 주소를 사용하므로 부족하다.
  - NAT를 사용한다면 출발지/도착지/포트번호를 바꾸게 되므로  End to End 통신을 침범하게 된다.
  - 차세대 버전인 IPv6가 필요하다.
- IPv6의 특징
  - 주소로 128비트를 사용한다.
    - 주소 두개 32 바이트 + 다른 헤더 부분 8 바이트
  - 라우팅 성능 향상과 QoS를 제공한다.
    - Flow Label을 사용해서 VOD는 먼저, HTTP는 조금 나중에 보내도록 스케줄링 할 수도 있다.
    - 자원을 낭비없이 사용 가능한 것이다.
  - 단편화를 허용하지 않는 단순한 고정길이 헤더로 라우팅 성능을 향상시킨다.

 

------

## IP Datagram Format



![img](https://blog.kakaocdn.net/dn/ASnH0/btqGyKB2EQY/gA1TkuqDVydTVxHWkENGkK/img.png)



 

- IPv6의 헤더를 살펴보자.
  - Version : IP의 버젼이 들어간다
  - Traffic Class : Priority라고도 한다. QoS를 위한 라벨이다.
  - Flow Label : QoS를 위한 라벨이다.
  - Payload Length : 페이로드(데이터)의 크기를 나타낸다.
  - Next Header : 고정길이 헤더를 사용하므로 Optional 헤더가 필요하면 헤더를 여러개 보내는데 이 때 사용한다. 또한 마지막 헤더일 시에 상위 계층 레이어를 표시하기도 한다.
  - Hop Limit : TTL과 같다.
- IPv6 데이터그램의 특징
  - IPv4보다 단순한 헤더를 사용해서 처리속도가 빠르다.
  - 고정길이 40바이트 헤더를 사용한다.
  - No Fragmentation allowed.
    - MTU가 작으면 ICMPv6를 이용해서 보고하고 드랍한다.
    - Fragmentation은 호스트에서 처리한다.

------

## IPv4와 IPv6 간 연동

- 터널링
  - Tunneling
  - IPv4라우터 사이로 IPv6 데이터그램이 지나가야 할 때 IPv6 데이터그램은 IPv4 페이로드에 실린다.
  - 즉 양 끝단의 IPv6 라우터는 IPv4로 통신하는 Endsystem처럼 취급된다.



# Network layer 5

>   Routing algorithms

## 라우팅 알고리즘

- 네트워크 상에는 여러 네트워크 장비들이 있다. 목적지까지 무작위 경로로 갈 순 없으니 경로를 설정해야 하는데 어떤 알고리즘을 사용할까?
- 라우팅 알고리즘의 분류 : Information
  - Global
    - 모든 라우터가 완전한 링크 정보를 알고 있다
    - Global한 라우팅 알고리즘을 Link State 알고리즘이라고 한다.
    - 다익스트라 알고리즘이 해당된다.
  - Decentralized
    - 한 라우터는 이웃한 라우더들로 가는 Link 정보와 이웃한 라우터와 목적지까지의 거리를 알고 있다.
    - Distance Vector 알고리즘이라고 한다.
    - 벨만-포드 알고리즘이 해당된다.
- 라우팅 알고리즘을 Cost에 따라 Static과 Dynamic으로도 구분할 수 있다.

------

## 다익스트라 알고리즘

- 다익스트라 알고리즘의 핵심 포인트
  - 다익스트라 알고리즘이 진행되면서 특정 노드에 이르는 최단경로를 발견하게 된다.
  - 특정 노드에서 시작할 때 발견한 다음 노드들 중 최단 경로로 갈 수 있는 노드가 최단경로가 확정된 노드가 된다.
  - 왜냐하면 다른 길로 돌아가더라도 그 거리보다 짧을 순 없기 때문이다.
  - 최단경로가 확정된 노드로 들어가서 다시 다른 노드에 대해 최단경로를 확정한다.
  - 즉 목적지까지의 최단 경로는 최단 경로들의 합이다
  - 헷갈리지 않게 스텝/노드들로 표를 그려가며 풀어보자.
- 시간복잡도는 일반적으로 O(n^2)이며 어떤 똑똑한 사람이 O(nlogn) 알고리즘을 발견했다.

------

## 벨만-포드 알고리즘

- 네트워크 전체 정보가 아닌 이웃한 라우터의 Link State와 그 라우터들의 목적지까지의 거리를 이용한다.
- x에서 y로 가는 최소 비용은 이웃한 라우터 v들에 대해  min{C(x,v) + Dv(y)}로 정의할 수 있다. 이를 벨만포드 방정식이라고 한다.
- Recursion 방식이다.

------

## Distance Vector란?

- Distance Vectorm 는 모든 목적지까지로 가는데 드는 비용 벡터이다.
  - 각 라우터(노드)들은 자신의 Distance Vector와 이웃 노드들 까지의 Cost를 알고 있어야 한다.
  - 전체 네트워크 상에서 모든 노드들은 이웃들끼리 Distance Vector를 교환한다.
  - 그렇게 정보가 퍼져나가면서 전체 네트워크의 Distance Vector가 업데이트된다.
  - 한 노드가 새로운 Distance Vector를 받았을 때 벨만-포드 방정식을 사용해서 자신의 Distance Vector를 업데이트한다.
- Distance Vector 알고리즘의 사이클
  - \1. 이웃으로 가는 링크의 코스트가 변하거나 이웃에게서 DV 업데이트를 받는다.
  - \2. 자신의 DV를 다시 벨만포드 알고리즘을 적용해서 업데이트하고 변화가 있으면 이웃에게 알린다.
  - \3. 대기한다.
- Count to Infinity 문제가 있다.
  - 각 노드 x, y, z가 루프를 이룬다고 생각해보자.
  - y -> x로 가는 코스트가 크게 상승하면 y는 자신의 DV를 업데이트 할 때 z의 DV를 참고한다.
  - 하지만 z는 사실 코스트가 크게 상승하기전 y의 DV를 이용한 DV를 가지고 있다.
  - DV를 의존하는 노드가 DV를 물어볼 때 INF로 대답해야 한다. ( Poisoned Reverse)

------

## Link State VS Distance Vector

- Message Complexity
  - Link State 알고리즘은 네트워크 크기가 커질 수록 한 노드가 처리해야하는 양이 매우 많아진다.
  - Distance Vector 알고리즘은 전체 네트워크 크기랑 상관없이 자신의 DV만 계산하면 된다.
- Speed of Convergence
  - Link State 알고리즘은 Link State가 브로드캐스팅 된 후에는 다익스트라 알고리즘을 계산하는 시간만 필요하다.
  - Distance Vector 알고리즘은 Louting Loop 문제와 규모가 커지면 Convergence가 잘 안된다.
- Robustness
  - Link State 알고리즘은 영향이 적다.
  - Distance Vector 알고리즘은 DV에 모든 목적지 정보가 들어가있기 때문에 파장이 크다.

------

## Dynamic Cost의 문제점

- 한 경로의 Cost가 낮으면 그 쪽으로 트래픽이 쏠린다.
- 그 경로의 Cost가 높아지면 다른 쪽을 트래픽이 쏠린다.
- 위와 같은 일이 계속 일어나면 Oscillation이 발생한다.
- 짧은 시간 내에 경로가 계속 바뀌면 In-Order 데이터 전송이 어려워지고 서로 다른 Topology로 라우팅 루프가 생기기 쉽다.



















