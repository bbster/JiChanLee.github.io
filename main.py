import sys
import fitz
import os
# print(os.listdir('/Users/bcd/Desktop/my_project/pdf'))
# file_list = os.listdir('/Users/bcd/Desktop/my_project/pdf')
#
#
#
# #


def parse(pdf_file_name):
    with fitz.open(pdf_file_name) as pdf_doc:
        page = pdf_doc.load_page(0)

        lines = page.get_text().strip().split('\n')

        # 기준은 "Category" 가 위치한 위치부터 파싱로직을 달리한다.
        target_position = lines.index('Category')

        # Order 정보 파싱
        order_info = lines[:target_position]
        divide_len = int(len(order_info) / 2)
        values = order_info[:divide_len]
        keys = order_info[divide_len:]
        keys = [key.replace(':', '') for key in keys]
        order_data = dict(zip(keys, values))

        # Table 파싱
        table_info = lines[target_position:]
        divide_len = int(len(table_info) / 2)
        values = table_info[divide_len:]
        keys = table_info[:divide_len]
        keys = [key.replace(':', '') for key in keys]
        table_data = dict(zip(keys, values))

        return order_data, table_data


if __name__ == '__main__':
    pdf_filename = sys.argv[1]
    # order_data, table_data = parse(f"file_path, file_name")
    order_data, table_data = parse(pdf_filename)
    print(order_data)
    print(table_data)
print("--------------------------------------------------------------------------------------------------------")

# 1. pdf 다운로드 한다. (java에서)
# 2. 다운로드 한 파일의 경로를 인수로, 파이썬 파일을 호출한다.
#  ex) python main.py {다운로드 파일 경로}
# 3. 다운로드 한 파일은 삭제한다.
