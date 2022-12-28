# Github
원격저장소 버전을 관리한다. 로컬저장소에서 github(원격저장소)에 버전을 올리거나(push) 받을(pull) 수 있다.


## 초기 원격저장소 설정
1. 깃헙에서 New Repository로 원격저장소 만들기(세부설정은 알아서)

2. ulr 확인하기 

   https://github.com/<span style="color:green">GitHub Username</span>/<span style="color:yellow">저장소이름</span>.git 으로 되어있다.

3. 로컬저장소에서 원격저장소 정보 설정하기
    
     깃헙 repository를 만들면 친절하게 코드도 알려준다.

     >git remote add origin 깃헙저장소주소

    ※ >git remote -v (원격저장소 정보를 확인할수 있음!)
    <!--당구장 뒤에는 인용이 안되네요... 어캐해야할지-->

---
## 사용법
![과정](https://i.ytimg.com/vi/0nqJKEh3YCc/maxresdefault.jpg)

### Push

>git push <원격저장소이름> <브랜치이름>

원격저장소로 번경사항(커밋)을 올림

※ 인증하라고 깃헙에서 뭐라뭐라할수도 있음(당황X)

### Pull

>git pull <원격저장소이름> <브랜치이름>

원격저장소로부터 변경된 내역을 받아와서 이력을 병함함

### Clone

>git clone <원격저장소이름>

원격저장소를 복제해서 가져옴

```
clone 과 알집 다운의 차이점
.git 폴더가 있고 없고
clone은 전 버전들을 전부 가져오지만
알집다운은 최신버전만 가져온다!
```
---

## Push Conflict

로컬과 원격저장소의 커밋 이력이 다른 경우 발생한다.

1. 원격저장소의 커밋을 로컬로 가져와서(pull)

2. 로컬에서 두 커밋을 병합(merge)

3. 다시 github으로 push

추가로 merge conflict가 있지만 내일 배워보도록 하자

---

## Gitignore

* 개발과정에서 버전 관리를 별도로 하지 않는 파일/디렉토리가 발생한다.(자동으로 만들어지는 cache, 개인정보 등)

* 이 경우 .gitignore 파일을 생성하고 해당 내용을 관리한다.

  <span style="color:red">주의! 이미 커밋된 파일은 삭제해야 적용됨</span>

[참고](https://www.toptal.com/developers/gitignore)