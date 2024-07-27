import re
import argparse

# 로그 파일에서 데이터를 읽어오는 함수
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# PK 추출 시간과 SUBK 추출 시간의 평균을 계산하는 함수
def calculate_averages(log_data):
    # 정규 표현식을 사용하여 PK 추출 시간과 SUBK 추출 시간 추출
    pk_times = re.findall(r'PK 추출 시간: ([\d\.]+) seconds', log_data)
    subk_times = re.findall(r'SUBK 추출 시간: ([\d\.]+) seconds', log_data)
    total_times = re.findall(r'총 추출 시간: ([\d\.]+) seconds', log_data)

    # 문자열을 float로 변환하여 리스트에 저장
    pk_times = [float(time) for time in pk_times]
    subk_times = [float(time) for time in subk_times]
    total_times = [float(time) for time in total_times]

    # 평균 계산
    pk_avg = sum(pk_times) / len(pk_times) if pk_times else 0
    subk_avg = sum(subk_times) / len(subk_times) if subk_times else 0
    total_avg = sum(total_times) / len(total_times) if total_times else 0

    return pk_avg, subk_avg, total_avg

if __name__ == "__main__":
    # 명령줄 인수 파싱
    parser = argparse.ArgumentParser(description='로그 파일에서 PK, SUBK 추출 시간의 평균을 계산하는 스크립트')
    parser.add_argument('file_path', type=str, help='로그 파일 경로')

    args = parser.parse_args()

    # 로그 파일 읽기
    log_data = read_log_file(args.file_path)

    # 평균 계산
    pk_avg, subk_avg, total_avg = calculate_averages(log_data)

    # 결과 출력
    print(f"PK 추출 시간의 평균: {pk_avg:.6f} seconds")
    print(f"SUBK 추출 시간의 평균: {subk_avg:.6f} seconds")
    print(f"총 추출 시간의 평균: {total_avg:.6f} seconds")