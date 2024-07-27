# API Call Scrtip
해당 스크립트는 작성된 JSON 데이터를 사용하여 API를 반복적으로 호출하고, 각 호출에 대한 응답 시간을 기록 후 평균 응답 시간을 계산한는 스크립트.
단일 프로세스와 멀티 프로세스 2개로 나누어 실행이 가능함.

## 파일설명

- `request_api_call_script.py` : API 호출을 수행하는 메인 스크립트.
- `run_multiple_processes.py`: 동일한 파라미터로 `request_api_call_script.py`를 여러 프로세스로 동시에 실행하는 스크립트.

## 사용법

### request_api_call_script.py 실행 방법

이 스크립트는 명령줄에서 실행할 수 있으며, 세 개의 인수를 필요함:

1. `json_path`: JSON 파일의 경로
2. `api_url`: API의 URL
3. `n`: API 호출 횟수

예시:

```sh
python request_api_call_script.py /path/to/example_dev.json http://localhost:8080/api/example/ 100
```

### 여러 프로세스로 실행하기 (run_multiple_processes.py)

run_multiple_processes.py 스크립트를 사용하여 동일한 파라미터로 request_api_call_script.py를 여러 프로세스로 동시에 실행할 수 있도록 만들었으며, 기본 설정으로 5개의 프로세스를 실행함.

#### 스크립트 내용

```python
import subprocess

# 실행할 스크립트 경로
script_path = "request_api_call_script.py"

# 동일한 파라미터 값 설정
json_path = "/path/to/example_dev.json"
api_url = "http://localhost:8080/api/example/"
n = 100

# 프로세스 리스트
processes = []

# 5개의 프로세스를 생성하여 동시에 실행
for _ in range(5):
    process = subprocess.Popen(["python3", script_path, json_path, api_url, str(n)])
    processes.append(process)

# 모든 프로세스가 종료될 때까지 대기
for process in processes:
    process.wait()
```

#### 실행방법

위의 스크립트를 실행하여 5개의 프로세스를 동시 실행할 수 있음.

예시:

```sh
python run_multiple_processes.py
```

## 성능 결과

`request_api_call_script.py`를 실행한 후, 각 요청의 응답 시간과 평균 응답 시간이 출력되도록 만들었음.

### 출력 예시

```sh
요청 1/100 가 0.1234 seconds 응답 완료
요청 2/100 가 0.2345 seconds 응답 완료
…
요청 100/100 가 0.3456 seconds 응답 완료

성능결과:
총 요청 수: 100
평균 응답 시간: 0.2345 seconds
중앙값 응답 시간: 0.2340 seconds
최대 응답 시간: 0.3456 seconds
최소 응답 시간: 0.1234 seconds
```

