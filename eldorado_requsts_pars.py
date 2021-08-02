import requests
import time

start_time = time.time()

def get_page_data(url):
    all_data = []

    r = requests.get(url)
    print(f'get {r.url}')
    all_data.append(r)


    return all_data

def main():

    num = 0
    for i in range(1, 183):
        url = f'https://www.eldorado.ru/search/catalog.php?q=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD&offset={str(num)}&utf'
        get_page_data(url)

        num += 36

if __name__ == '__main__':
    main()

    end_time = time.time() - start_time
    print(end_time)