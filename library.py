import json
class Book:
    def __init__(self, name, author, year, price, status):
        self.name = name
        self.author = author
        self.year = year
        self.price = price
        self.status = status

    def show_info_book(self):
        return (f"نام کتاب: {self.name} نویسنده: {self.author} سال انتشار:{self.year} قیمت:"
                f" {self.price} وضعیت: {self.status}")
    def __str__(self):
        return f"{self.name} | {self.author} | {self.status} | {self.price}"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrows_book(self, name):
        self.borrowed_books.append(name)
        return self.borrowed_books


class Library:
    def __init__(self):
        self.lst_books = []
        self.lst_users=[]
        self.load_books()
        self.load_users()

    def save_books(self):
        data=[]
        for book in self.lst_books:
            data.append({"name":book.name,"author":book.author,"price":book.price,"year":book.year,"status":book.status})
        with open("books.json","w",encoding="utf-8")as file:
            json.dump(data,file,ensure_ascii=False,indent=4)

    def load_books(self):
        try:
            with open("books.json","r",encoding='utf-8')as file:
                data=json.load(file)
                for item in data:
                    book=Book(item["name"],item["author"],item["year"],item["price"],item["status"])
                    self.lst_books.append(book)
        except FileNotFoundError:
            pass

    def save_users(self):
        data=[]
        for user in self.lst_users:
            data.append({"name":user.name,"user_id":user.user_id,"borrowed_books":[book.name for book in
                                                                                   user.borrowed_books]})
            with open("users.json","w",encoding="utf-8")as file:
                json.dump(data,file,ensure_ascii=False,indent=4)

    def load_users(self):
        try:
            with open("users.json","r",encoding="utf-8")as file:
                data=json.load(file)
                for item in data:
                    user=User(item["name"],item["user_id"])
                    for book_name in item["borrowed_books"]:
                        for book in self.lst_books:
                            if book.name==book_name:
                                user.borrowed_books.append(book)
                                self.lst_users.append(user)
        except FileNotFoundError:
            pass

    def add_user(self,user):
        self.lst_users.append(user)
        self.save_users()

    def add_book(self,book):
        self.lst_books.append(book)
        self.save_books()

    def remove_book(self, number):
        if number<= len(self.lst_books) and number>0:
            self.lst_books.pop(number-1)
            self.save_books()
            return "removed successfully"
        return "not found"

    def show_book(self):
        result = []
        for i, book in enumerate(self.lst_books, start=1):
            result.append(f"{i} - {book.name} | {book.author} | {book.price} | {book.status}")
        return result


    def search_book(self, name):
        for book in self.lst_books:
            if name in book.name:
                return book.show_info_book()
        return "not found"


    def borrow_book(self, user, book):
        if book in self.lst_books and book.status == "موجود":
            book.status = "امانت داده شد"
            user.borrowed_books.append(book)
            self.save_books()
            self.save_users()
            return "کتاب با موفقیت امانت داده شد"
        else:
            return "کتاب در دسترس نیست"


    def return_book(self, user, book):
        if book in user.borrowed_books:
            book.status = "موجود"
            user.borrowed_books.remove(book)
            self.save_books()
            self.save_users()
            return "کتاب با موفقیت بس گرفته شد"
        return "کتاب موجود نیست"

    # def find_user(self,user_idee):
    #     for user in self.lst_users:
    #         if user.user_id==user_idee:
    #             return user
    #         else:
    #             return None

# book1=Book("بینوایان","ویکتور هوگو",2015,250000,"موجود")
# book2=Book("تنهایی","محمد روشنگر",2012,195000,"موجود")

# library1=Library()
# library1.add_book(book1)
# library1.add_book(book2)
# user1=User("sonia","soni_013")
# library1.borrow_book(user1,book1)
# library1.show_book()
# library1.return_book(user1,book1)
# library1.show_book()
# print(library1.search_book("بینوایان"))
# print(library1.remove_book(2))
# library1.show_book()
