# django를 이용한 백엔드 웹 프로젝트

---

> ## Django의 장점

>> 1.  MTV구조로 각 복잡하게 코드가 엮이지 않는다 ex) url패턴은 url.py에만, DB관련은 model.py에만 작성가는한것 등등.
>> 2.  제네릭 뷰를 이용해 코드 가독성과 빠른 웹 개발이 가능하다.
>> 3.  auth가 기본 내장되어있어 외부에서 끌어서 쓰지 않아도 로그인에 대한 보안이 확실하다.
>> 4.  session또한 기본 내장 및 암호화가 기본으로 되어있어 따로 코드를 만지지 않아도 보안을 시켜준다.
>> 5.  csrf token으로 제 3자가 해킹 접근시 django가 이를 막아준다.
>> 6.  이미 Instargram, Dropbox에서는 Django를 채택하여 구현하여 좋은 프레임워크임을 알려주었다.
>> 7.  Django의 커뮤니티는 활발하여 어디서나 문제점을 해결 할 수 있다.
>> 8.  마이그레이션을 할 때 따로 코드를 작성하지않아도 Django가 알아서 만들어주고, 이것을 테이블의 컬럼속성에 적용시킨다.

---

> ## Django의 단점

>> 1.  빠른 웹개발이 가능하지만 개발자가 미리 공부해야할 부분이 많은거같다.
>> 2.  특히 제네릭 뷰의 공부를 많이해야 정말 빠른 웹개발을 할 수 있다.

---

> ## 내가 구현한 Django 기능

>> 1.  글 목록 리스트
>> 2.  글의 상세정보
>> 3.  글의 수정기능
>> 4.  새 글 작성기능
>> 5.  글 삭제기능
>> 6.  회원가입 기능
>> 7.  로그인 기능
>> 8.  로그인을 하지않고 글 목록기능에 접근시 로그인 url로 리다이렉트시킴
>> 9.  회원가입시 메세지 띄우기, 아이디 혹은 비밀번호가 틀렸을 때 메세지 띄우기 기능
>> 10. session기능 사용 (로그인 시 세션 생성, 로그아웃시 세션 삭제)

---

> ## board 파일
>
> 글과 관련된 로직들이 모여있는 곳

---

> ## user 파일
>
> 회원과 관련된 로직들이 모여있는 곳

---

> ## newApp 파일
>
> Django서버와 관련된 파일들이 모여있는 곳

---

> ## Django 서버 실행방법
> ```python manage.py runserver```
> 회원가입하시고 이용해 보세요~
