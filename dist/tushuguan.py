class Book:
    def __init__(self,name,author,comment,state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        status = '未借出'
        if self.state == 1:
            status = '已借出'
        return  '书名：《%s》 作者：%s  推荐语：%s\n状态：%s'%(self.name,self.author,self.comment,status)


class BookManager:
    books = []
    def __init__(self):
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。')
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
    def menu(self):
        print('欢迎使用图书管理系统')
        while True:
            print('1.查询所以书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.返回')
            choice = int(input('请输入数字选择对应功能：' ))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                print('感谢使用！')
                break
    def show_all_book(self):
        print('书籍信息如下：')
        for book in self.books:
            print(book)
            print('')
    def  add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者：')
        new_comment = input('请输入推荐语')
        new_book = Book(new_name,new_author,new_comment)
        self.books.append(new_book)
        print('添加书籍成功')
    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None

    def lend_book(self):
        name = input('请输入书籍名称：')
        res = self.check_book(name)
        if res != None:
            if res.state == 1:
                print('已借出!')
            else:
                print('借阅成功！')
        else:
            print('没有这本书！')
    def return_book(self):
        name = input('请输入归还书籍名称“')
        res = self.check_book(name)
        if res == None:
            print('没有这本书！')
        else:
            if res.state == 0:
                print('书被借走拉！')
            else:
                print('归还成功！')
                res.state == 0
tata = BookManager()
tata.menu()