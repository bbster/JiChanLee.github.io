import csv

with open('20221117_luisa_crawl_data_JC.csv') as f:
    detail_urls = []
    csv_rows = csv.DictReader(f)
    for idx, row in enumerate(csv_rows):
        if idx == 0:
            detail_urls.append(row.keys())
            break

print(detail_urls)
