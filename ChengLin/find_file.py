import os

base_path = 'D:\\Users\\Desktop\\111'
search_exts = '.txt .md .nc .mpf'.split(" ")
search_word = 'G5.1 T'.split(" ")

def find():
    for root, dirs, files in os.walk(base_path):
        for filename in files:
            for ext in search_exts:
                if(filename.endswith(ext)): #判断文件类型
                    file = os.path.join(root, filename) #获得打开文件路径
                    search_file(file, search_word)

def search_file(file, word):
    with open(file, 'r') as f:
        for num, content in enumerate(f.readlines(), 1):
            for key in word:
                if str(key) in content:
                    print(f'found <{content}> at Line {num} in file: {file}')


if __name__ == "__main__":
    find()