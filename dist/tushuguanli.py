class Book:

    def __init__(self, name, author, comment, state=0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)


class BookManager:
    authors = []

    def __init__(self):
        book1 = Book('撒哈拉的故事', '三毛', '我每想你一次，天上便落下一粒沙，从此便有了撒哈拉。')
        book2 = Book('梦里花落知多少', '三毛', '人人都曾拥有荷西，虽然他终会离去。')
        book3 = Book('月亮与六便士', '毛姆', '满地都是六便士，他却抬头看见了月亮。')
        self.books = [book1, book2, book3]
        self.authors.append(book1.author)
        self.authors.append(book2.author)
        self.authors.append(book3.author)

    def menu(self):
        while True:
            print('1.查询书籍')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_author_book()
            else:
                print('感谢使用！')
                break

    def show_author_book(self):
        author = input('请输入想查询作家的名称：')
        if author in self.authors:
            print(author + '的作品有：')
            for book in self.books:
                if book.author == author:
                    print(book)
        else:
            print('很可惜，我们暂时没有收录这位作者的作品')


manager = BookManager()
manager.menu()