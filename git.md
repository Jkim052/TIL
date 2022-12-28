# Git
분산 버전 관리툴 

"리누스 토르발스" 아저씨가 만듬

```
버전 관리의 중요성 
  
  졸논1.hwp
  졸논2.hwp
  졸논3.hwp
  졸논최종.hwp

자료 간의 차이(diff)를 모른다
  
  졸논1.hwp >> 뼈대
  졸논2.hwp >> 서론 본론 결론 작성
  졸논3.hwp >> 그래프, 그림, 참조 삽입

차이(diff)와 수정 이유를 메세지로 남기려 한다. 백업과 구분을 쉽게 해준다.
```
---
## 중앙 VS 분산

* 중앙집중식버전관리시스템

  중앙에서 버전을 관리하고 파일을 개개인이 받아 사용

  ![중앙](https://t1.daumcdn.net/cfile/tistory/184C803F514047D41D)

* 분산버전관리시스템(DVCS)

  원격 저장소(remote repository)를 통하여 협업하고, 모든 히스토리를 만들어 클라이언트들이 공유
  
  ※로컬에서도 버전관리
  

  ![분산](https://t1.daumcdn.net/cfile/tistory/2511743F514047D442)

----

## 깃 장소

1)작업하면 2) add하여 Staging area에 모아 3) commit으로 버전 기록

* <span style="color:red">Working Directory</span> : 파일의 변경사항


* <span style="color:green">Staging Area</span> : 버전으로 기록하기 위한 파일 변경사항의 목록


* Repository : 커밋(버전)들이 기록되는 곳

---

## 깃 내부 명령어 

* git init
* git add 파일 및 문서명
* git commit -m '커밋메세지'
* git status
    <details>
    <summary>자세한 내용</summary>
    <div markdown="1"> 

    * Tracked : 이전부터 버전으로 관리되고 있는 파일
      * Unmodified : git status에 나타나지 않음(변경사항 없음)
      * Modified : Changes not staged for commit(변경사항이 stage에 올라가지 않음)
      * Staged : Changes to be committed(변경사항이 stage에 올라가 커밋될 준비를 마침)
    * Untracked : 버전으로 관리된 적 없는 파일(새로 만든 경우)

    </div>
    </details>

* git log

  * 깃 내부 커밋과정

  
  ![깃커밋](/b/%EA%B9%83%EB%82%B4%EB%B6%80%EC%BB%A4%EB%B0%8B%EA%B3%BC%EC%A0%95.png)

  * 깃 커밋 상태확인
    <details>
    <summary>누르던가 말던가</summary>
    <div markdown="1"> 

    단어가 조금 다르긴 하지만 
  
    staged snapshot은 staging area로

    committed history는 repository로 이해하면 될 듯

    사실상 같은 의미이다.

    </div>
    </details>
  
      ![깃로그](/b/%EA%B9%83%EC%83%81%ED%83%9C%ED%99%95%EC%9D%B8.png)

