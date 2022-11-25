# 로그인 정보를 확인하는 파일
# https://wikidocs.net/85739(참고?)
# main으로부터 받은 id,pw를 on국민에 넣었을 때의 웹페이지를 크롤링하여 국민대 학생인지 확인한다
# view-source:https://portal.kookmin.ac.kr/por/ln -570line
# view-source:https://sso.kookmin.ac.kr/sso/error.jsp

# 일단 로그인 권한을 True로 설정해준다. => 로그인 정보를 받아오면 변경해야함
class Session:
    def CheckPermission():
        return True