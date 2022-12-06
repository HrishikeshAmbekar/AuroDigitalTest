from bisect import *

class OrderBooks:
    def __init__(self):
        self.books = {}
    
    def addorder(self, l, t):
        l.insert(bisect_right(l, t), t)


    def matchorders(self, book):
        buys = self.books[book][0]
        sells = self.books[book][1]
        r = len(buys) - 1
        l = 0
        while r >= 0 and l < len(sells):
            if buys[r][0] <= sells[l][0]:
                if buys[r][1] < sells[l][1]:
                    sells[l][2] -= buys[r][2]
                    # buys.pop()
                    r -= 1
                elif buys[r][1] > sells[l][1]:
                    buys[r][2] -= sells[l][2]
                    # sells.remove()
                    l += 1
                else:
                    l += 1
                    r -= 1
            else:
                break
        self.books[book][0] = self.books[book][0][:r+1]
        self.books[book][1] = self.books[book][1][l:]


    def add_order(self, book, operation, price, volume, order_id):
        if book not in self.books:
            self.books[book] = [[], []]
        
        operation = 1 if operation == "SELL" else 0


        self.addorder(self.books[book][operation], (price, volume, order_id))
        self.match_orders(book)

    def delete_order(self, book, orderid):
        if book not in self.books:
            return
        buys = self.books[book][0]
        sells = self.books[book][1]
        idx = -1
        for i in range(len(buys)):
            a, b, c = buys[i]
            if c == orderid:
                idx = i
        if idx != -1:
            buys.pop(idx)

        
        idx = -1
        for i in range(len(sells)):
            a, b, c = sells[i]
            if c == orderid:
                idx = i
        if idx != -1:
            sells.pop(idx)

    def readXML(self, filepath):
        #Read the XML file and process each line using the above functions
        pass


