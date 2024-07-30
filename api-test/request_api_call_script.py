import requests
import json
import time
import statistics
import argparse

# json 파일에서 데이터를 읽어오는 함수
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
# API 호출 함수
def call_api(json_data, url, n):
    # 파라미터 정보
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = json_data

    # api 호출 시간을 저장할 리스트 초기화
    response_times = []

    # 전체 시작 시간 기록
    total_start_time = time.time()

    # n번 만큼 api 반복 호출
    for i in range(n):
        # 시작 시간 기록
        start_time = time.time()
        try:
            response = requests.post(url, headers=headers, data=body)
            # 끝난 시간 기록
            end_time = time.time()
            response_time = end_time - start_time
            response_times.append(response_time)

            print(f"요청 {i+1}/{n} 가 {response_time:.4f} seconds 응답 완료")
        except Exception as e:
            print(f"이슈 : {e}")

    # 전체 끝난 시간 기록
    total_end_time = time.time()
    total_elapsed_time = total_end_time - total_start_time

    # 결과 출력
    print("\n성능결과:")
    print(f"총 요청 수: {n}")
    if response_times:
        valid_times = [t for t in response_times if t is not None]
        if valid_times:
            print(f"평균 응답 시간: {statistics.mean(valid_times):.4f} seconds")
            print(f"최대 응답 시간: {max(valid_times):.4f} seconds")
            print(f"최소 응답 시간: {min(valid_times):.4f} seconds")
        else:
            print("유효한 응답 시간이 없음")
    else:
        print("응답 시간이 없음.")

    print(f"\n총 걸린 시간: {total_elapsed_time:.4f} seconds")

# 메인 함수
def main(json_path, api_url, n):
    # json 파일 읽기
    json_data = read_json_file(json_path)

    # API 호출
    call_api(json_data, api_url, n)

if __name__ == "__main__":
    # 명령줄 인수 파싱
    parser = argparse.ArgumentParser(description='API 테스트 스크립트')
    parser.add_argument('json_path', type=str, help='JSON 파일 경로')
    parser.add_argument('api_url', type=str, help='API URL 경로')
    parser.add_argument('n', type=int, help='API 호출 횟수')

    args = parser.parse_args()

    # 메인 함수 호출
    main(args.json_path, args.api_url, args.n)