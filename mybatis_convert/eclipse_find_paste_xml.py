import pyautogui

# 프로그램 실행시 주의사항 
# 1. capslock버튼 비활성화하기 

# 문자열을 문자 배열로 반환 
def convertStringToCharList(str):
    word = str
    lst = []

    for i in word:
        lst.append(i)

    return lst

# 텍스트 찾기 창 열기 
def openFindReplacePopup():
    with pyautogui.hold('ctrl'):
        pyautogui.press(['f'])
    #pyautogui.hotkey('ctrl', 'shift', 'esc')

def moveTabAtFindReplacePopup(max):
    for i in range(0, max):
        pyautogui.keyDown("\t")

# text find / replace 
def callFindReplaceText(condition, newStr):
    openFindReplacePopup()
    pyautogui.press(convertStringToCharList(condition))
    moveTabAtFindReplacePopup(1)
    pyautogui.press(convertStringToCharList(newStr))
    moveTabAtFindReplacePopup(7)
    pyautogui.keyDown("enter")   
    pyautogui.keyDown("esc")   
    pyautogui.sleep(3)
    with pyautogui.hold('ctrl'):
        pyautogui.press(['s'])
    pyautogui.sleep(3)
    

# 메인함수 실행 부분 
screen = ""
for w in pyautogui.getAllWindows():
    if 'Spring Tool Suite 4' in w.title:
        screen = w
        print(w.title)

if screen != "":
    screen.activate()

    
    # ]]> 지우기
    callFindReplaceText('\]\]>', '' )

    # mybatis 선언 
    callFindReplaceText('\<!DOCTYPE sqlMap PUBLIC "-//iBATIS.com//DTD SQL Map 2.0//EN" "http://ibatis.apache.org/dtd/sql-map-2.dtd"\>', '<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">')

    # nameSpace 
    callFindReplaceText('\<sqlMap namespace="([a-z|A-Z|0-9|_]+)"\>', '<mapper namespace="패키지명 수정.$1Repository">' )
    
    callFindReplaceText('\</sqlMap\>', '</mapper>' )

    #  parameterClass="map" => ""
    callFindReplaceText('parameterClass="map"', '' )

    # resultClass="hmap" => resultType="hashmap"
    callFindReplaceText('resultClass="hmap"', 'resultType="hashmap"' )

    #  #([a-z|A-Z|0-9|_]+)#  =>  #{$1}    
    callFindReplaceText('#([a-z|A-Z|0-9|_]+)#', '#{$1}' )

    # <![CDATA[ 지우기
    callFindReplaceText('<!\[CDATA\[', '' )


    # (주의사항 prepare="and" 조건은 제외함. and 키워드를 쿼리에 추가해야하기 때문에 수동으로 고칠 것) 
    # before : \<isPropertyAvailable property="([a-z|A-Z|0-9|_]+)"\>  after : <if test="@org.apache.commons.lang3.StringUtils@anyNotNull($1)">        
    callFindReplaceText('\<isPropertyAvailable property="([a-z|A-Z|0-9|_]+)"\>', '<if test="@org.apache.commons.lang3.StringUtils@anyNotNull($1)">' )

    # before : \<isNotEmpty property="([a-z|A-Z|0-9|_]+)"\> after : <if test="@org.apache.commons.lang3.StringUtils@isNotEmpty($1)">
    callFindReplaceText('\<isNotEmpty property="([a-z|A-Z|0-9|_]+)"\>', '<if test="@org.apache.commons.lang3.StringUtils@isNotEmpty($1)">' )

    # before : \<isNotPropertyAvailable property="([a-z|A-Z|0-9|_]+)"\> after : <if test="!@org.apache.commons.lang3.StringUtils@anyNotNull($1)">     
    callFindReplaceText('\<isNotPropertyAvailable property="([a-z|A-Z|0-9|_]+)"\>', '<if test="!@org.apache.commons.lang3.StringUtils@anyNotNull($1)">' )

    # before : \<isEmpty property="([a-z|A-Z|0-9|_]+)"\> after : <if test="@org.apache.commons.lang3.StringUtils@isEmpty($1)">     
    callFindReplaceText('\<isEmpty property="([a-z|A-Z|0-9|_]+)"\>', '<if test="@org.apache.commons.lang3.StringUtils@isEmpty($1)">' )

    # before : \<isNotEqual property="([a-z|A-Z|0-9|_]+)" compareValue="([a-z|A-Z|0-9|_|-|@|.]+)"\>  after: <if test="$1 ne '$2'">
    callFindReplaceText('\<isNotEqual property="([a-z|A-Z|0-9|_]+)" compareValue="([a-z|A-Z|0-9|_|-|@|.]+)"\>', '<if test="$1 != \'$2\'">' )
    callFindReplaceText('\<isNotEqual property="([a-z|A-Z|0-9|_]+)" compareValue="-1"\>', '<if test="pageSize != -1">' )

    # before : \<isEqual property="([a-z|A-Z|0-9|_]+)" compareValue="([a-z|A-Z|0-9|_|-|@|.]+)"\> after: <if test="$1 eq '$2'">  
    callFindReplaceText('\<isEqual property="([a-z|A-Z|0-9|_]+)" compareValue="([a-z|A-Z|0-9|_|-|@|.|@|.]+)"\>', '<if test="$1 == \'$2\'">' )
    callFindReplaceText('\<isEqual property="([a-z|A-Z|0-9|_]+)" compareValue="-1', '<if test="$1 == -1">' )

    # 종료 태그 before : \</(isPropertyAvailable|isNotPropertyAvailable|isNotEqual|isEqual|isNotEmpty|isEmpty)\>  after : </if>     
    callFindReplaceText('\</(isPropertyAvailable|isNotPropertyAvailable|isNotEqual|isEqual|isNotEmpty|isEmpty)\>', '</if>' )

    callFindReplaceText('/\* (.+) \*/', '' )

    # 값  비교 (양옆에 공백이 있다는 가정하에 수정 )
    callFindReplaceText(' >= ', ' <![CDATA[ >= ]]> ')
    callFindReplaceText(' > ', ' <![CDATA[ > ]]> ')
    callFindReplaceText(' <= ', ' <![CDATA[ <= ]]> ')
    callFindReplaceText(' < ', ' <![CDATA[ < ]]> ')
    callFindReplaceText(' <> ', ' <![CDATA[ <> ]]> ')

    # iterate 
    #GATE_IDS[]# 
    callFindReplaceText('#([a-z|A-Z|0-9|_]+)\[\]#', '#{$1}' )
    callFindReplaceText('\<iterate prepend="([a-z|A-Z|0-9|_]+)" property="([a-z|A-Z|0-9|_]+)" open="\(" close="\)" conjunction=","\>', \
                        '$1 <foreach item="$2" collection="$2" open="(" separator="," close=")">')
    callFindReplaceText('\</iterate\>', '</foreach>')


    # dynamic 
    callFindReplaceText('\<dynamic prepend="WHERE"\>', '<trim prefix="WHERE" prefixOverrides="AND|OR">')

    callFindReplaceText('\<dynamic prepend="ORDER BY"\>', '<trim prefix="ORDER BY">')



    callFindReplaceText('\</dynamic\>', '</trim>')
    print("정상변경완료!")
    print("정상변경완료!")
    print("정상변경완료!")
    print("정상변경완료!")


print("종료!!")
print("종료!!")
print("종료!!")
print("종료!!")
print("종료!!")