import requests


def upload_file_example():
    url = "http://127.0.0.1:5000/predict"

    file_stream = open('image.jpeg', 'rb')
    files = {'file': file_stream}
    try:
        r = requests.post(url, files=files)
        print(r.text)
    finally:
        file_stream.close()


if __name__ == '__main__':
    upload_file_example()
