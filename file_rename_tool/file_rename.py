import os, sys
import subprocess

### 상수 선언 ###
CONST_COMMAND = "ls" # 현재 디렉터리의 파일내역 출력

# Python에서 외부 명령어를 실행하고 결과를 가져오는 메소드
def getCallResult(CONST_COMMAND):
    fd_popen = subprocess.Popen(CONST_COMMAND.split(), stdout = subprocess.PIPE).stdout
    data = fd_popen.read()
    fd_popen.close()
    return data

# file이름을 일괄 변경하는 메서드
def file_rename(arg1, arg2, arg3):
    fname = getCallResult(CONST_COMMAND)
    fname = fname.decode("utf-8")

    num = 1

    while(True):
        index = fname.find('\n')

        if(index == -1):
            break

        filename = fname[:index]
        fname = fname[index + 1:]
        
        # 이 프로그램과 이름 변경대상이 아닌 확장자의 경우 변경대상에서 제외
        if(filename.find('.' + arg3) == -1 or filename == 'file_rename.py'):
            continue

        cmd = "mv " + filename + ' ' + arg1 + str(num) + '.' + arg2
    
        os.system(cmd)

        num += 1

# argv[1] -> filename format
# argv[2] -> 확장자
# argv[3] -> 변경대상 확장자
file_rename(sys.argv[1], sys.argv[2], sys.argv[3])
