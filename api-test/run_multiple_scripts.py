import subprocess

# 실행할 스크립트 경로
script_path = "request_api_call_script.py"

# 동일한 파라미터 값 설정
json_path = "/path/to/example_dev.json"
api_url = "http://localhost:8080/api/example"
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