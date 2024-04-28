@REM 가상환경 만들기 python -m venv <가상환경이름>
python -m venv venv 

@REM windows에서 실행
cd venv/Scripts
source ./venv/Scripts/activate

@REM 필요한 의존 패키지 설치
python.exe -m pip install --upgrade pip
pip install -r ./requiremets.txt

@REM 패키지 setup 로 시작하기
python setup.py install

@REM 패키지 poetry 로 시작하기 
poetry new @REM 패키지 생성, 안해도 됨
poetry install


@REM 번외
@REM 패키지 setup 로 배포 하기 (아래 둘 중 하나 사용)
python setup.py install
pip install -e .
python -m twine upload dist/*

@REM 패키지 poetry로 배포하기 
poetry build 
poetry publish