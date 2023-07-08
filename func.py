class Books():
    def __init__(self):
        self.books={}

    def add_book(self,nom,muallif) :
      self.books[nom]=muallif

    def get_books(self):
        return self.books

    def search_book(self,nomi):
        result=[]

        for nom1,price in self.books.items():
            if nom1==nomi:
                result.append(price) 

        if not result:
            return f'bu kitob yoq'
        return result

kitob=Books()

kitob.add_book('python1',2500)
kitob.add_book('python2',2700)
kitob.add_book('python3',3000)

print(kitob.search_book('python2'))