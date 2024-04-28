@REM 가상환경 만들기 python -m venv <가상환경이름>
python -m venv venv 

@REM windows에서 실행
cd venv/Scripts
source ./venv/Scripts/activate

@REM 필요한 의존 패키지 설치
python.exe -m pip install --upgrade pip
pip install -r ./requiremets.txt

@REM 패키지 setup 
python setup.py install
