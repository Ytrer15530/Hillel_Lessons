import requests
from bs4 import BeautifulSoup

URL = 'https://hard.rozetka.com.ua/videocards/c80087/'
response = requests.get(URL)
# print(response)  # <Response [200]>
# print(response.url)
# print(response.status_code)
# print(response.content)
# print(response.headers['content-type'])
# print(response.encoding)
bs = BeautifulSoup(response.text, "lxml")
# print(bs)
# temp = bs.find('span', 'goods-tile__title')
# print(temp)
# print(temp.text)

# titles = bs.findAll('span', 'goods-tile__title')
# print(titles)
# #
# for title in titles:
#     print(title.text)


images = bs.findAll('img', 'ng-lazyloaded')
# print(images)
images_links = []
for image in images:
    images_links.append(image.get("src"))
#
# print(images_links)
#
current_file = 1

for link in images_links:
    print(f"Downloading {current_file} from {len(images_links)}...")
    folder_name = "rozetka_images/"
    file_name = link[link.rfind('/') + 1:]
    # print(file_name)
    result = requests.get(link, allow_redirects=True)
    open(folder_name + file_name, 'wb').write(result.content)
    current_file += 1
