import requests
from bs4 import BeautifulSoup



# # ชุดนอน
# with open('ชุดนอน.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         print(code)
#         # print(code[3])

# # ชุดนอนไม่ได้นอน agent
with open('ชุดนอนไม่ได้นอน.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    x = soup.find('title').text
    print(x)
   
for name in soup.find_all('b'):
    if "รหัสชุด" in name.text:
        code = name.text.split()
        # print(code)
        print(code[3])

# ชุดนอนไม่ได้นอน not agent
# with open('ชุดนอนไม่ได้นอน.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)

# # รหัสสินค้า
# for name in soup.find_all('div'):
#     if "รหัส" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[2])

# ราคา
# for name in soup.find_all('b'):
#     if "บาท" in name.text:
#         price = name.text.split()
#         # print(code)
#         print(price[0])


# # ชุดซีทรู
# with open('ชุดซีทรู.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         print(code[1])

        # print((code[1]),(code[3]))

# ชุดชั้นในเซ็กซี่
# with open('ชุดชั้นในเซ็กซี่.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[3])

# # ชุดกี่เพ้า
# with open('ชุดกี่เพ้า.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[3])

# # ชุดนักเรียนญี่ปุ่น
# with open('ชุดนักเรียนญี่ปุ่น.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[3])

# # ชุดพยาบาล
# with open('ชุดพยาบาล.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[3])

# # จีสตริง
# with open('จีสตริง.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[3])

# # ชุดเซ็กซี่
# with open('ชุดเซ็กซี่.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         print(code)
#         # print(code[1])

# # ชุดบอดี้สูท
# with open('ชุดบอดี้สูท.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         print(code)
#         # print(code[1])

# # ถุงน่อง
# with open('ถุงน่อง.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         print(code)
#         # print(code[1])

# # ชุดกระต่าย
# with open('ชุดกระต่าย.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[1])

# # ชุดเมด
# with open('ชุดเมด.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[3])

# # ชุดลายเสือ
# with open('ชุดลายเสือ.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[1])

# # ชุดคอสเพลย์
# with open('ชุดคอสเพลย์.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[3])

# ชุดกิโมโน
# with open('ชุดกิโมโน.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         # print(code)
#         print(code[1])

# # ชุดนอนคนอ้วน
# with open('ชุดนอนคนอ้วน.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
#     x = soup.find('title').text
#     print(x)
   
# for name in soup.find_all('b'):
#     if "รหัสชุด" in name.text:
#         code = name.text.split()
#         print(code)
#         # print(code[1])