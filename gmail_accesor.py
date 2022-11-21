import imaplib
import email
import os


def remove_files(dir_path: str) -> str:
    if os.path.exists(dir_path):
        for file in os.scandir(dir_path):
            print(f'delete: {file.path}')
            os.remove(file.path)


with imaplib.IMAP4_SSL('imap.gmail.com', port=993) as imap:  # gmail 서버 connect
    directory_path = 'your file directory'
    imap.login('your email', 'your password')  # imap을 통해 로그인
    # imap.list()  # Gmail 왼쪽 메뉴 리스트 (받은편지함, 라벨 등)

    imap.select('inbox or label')  # imap list 중 select 하여 해당 UID 추출
    _, message_numbers = imap.uid('search', None, 'UNSEEN')  # 'ALL' or 'SEEN' or 'UNSEEN'메일함에서 읽지 않은 메일만 검색하여 UID 추출

    for idx, message_number in enumerate(message_numbers[0].split()):  # byte data split하여 UID 하나씩 넘김
        _, data = imap.uid('fetch', message_number, '(RFC822)')  # UID를 통해 메시지 정보 가져옴(type: tuple)
        # imap.store(message_number, '+FLAGS', '\\SEEN')  # -Flags는 안읽음 처리 +Flags는 읽음 처리

        # data[0][0]에는 단일 메일 UID값이 나오고 data[0][1]에는 메일 내용이 닮기는것 같음
        message = email.message_from_bytes(data[0][1])

        if message.is_multipart():  # 메일 내부에 여러 파트가 나눠 있는지 체크 하는 기능 같음 -> text/plain, application/file_type 등
            for part in message.walk():  # message generator
                if part.get_content_type() == "application/pdf":  # 컨텐츠 타입이 application/pdf 타입인것만
                    file_name = part.get_filename()
                    file_name = file_name.split(".")[0]
                    file_name = f'{file_name}_{idx+1}.pdf'
                    print(f'{idx+1}: {file_name}')
                    with open(f'{directory_path}{file_name}', 'wb') as fp:  # 파일은 문자열이 아니기 때문에 wb옵션(write,binary)
                        fp.write(part.get_payload(decode=True))

    imap.close()
    imap.logout()
    # Todo Add Text Extractor Function

    # Todo Add Insert t_stocks Query

    # delete pdf file
    remove_files(directory_path)
