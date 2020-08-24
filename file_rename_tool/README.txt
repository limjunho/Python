argv[1] -> 변경할 파일명 format
argv[2] -> 변경할 확장자
argv[3] -> 변경대상 확장자

ex1) $ python3 file_rename.py test txt c
확장자가 .c인 파일을 모두 test.txt형식으로 변경

ex2) 확장자가 jpg인 파일을 모두 png로 바꾸고 기존의 png파일과 함께 pic.png형식으로 바꾸기
$ python3 file_rename.py test png jpg ; python3 file_rename.py pic png png
