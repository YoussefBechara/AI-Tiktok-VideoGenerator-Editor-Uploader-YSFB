from mega import Mega
import sys

def upload_file(email, password, file_path, description):
    mega = Mega()
    m = mega.login(email, password)
    uploaded_file = m.upload(file_path, dest_filename=description)
    link = m.get_upload_link(uploaded_file)
    print(f'Your file is available at: {link}')

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python mega_upload.py <email> <password> <file_path> <description>")
        sys.exit(1)

    email = sys.argv[1]
    password = sys.argv[2]
    file_path = sys.argv[3]
    description = sys.argv[4]

    upload_file(email, password, file_path, description)