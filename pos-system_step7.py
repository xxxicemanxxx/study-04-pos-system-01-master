import pandas as pd
import datetime

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price
#課題7_レシートファイル（テキスト）出力
class Fail:
    def __init__(self):
        now = datetime.datetime.now()
        self.failname = now.strftime('%Y%m%d_%H%M%S') 

    def file_write(self,str):
        #with openにすれば自動でファイルが閉じる　　引数　、mode='w'書き込み用、encoding = utf-8-sig：デフォルト状態
        #mode='a'追記
        with open("receipt_fail_{}.txt".format(self.failname),mode='a',encoding = "utf-8-sig") as log_file:
            log_file.write(str+"\n")
            #print(str)

### オーダークラス
class Order:
    #def __init__(self,item_master):
    def __init__(self):
        self.file_seve = Fail()
        self.item_master = []
        self.all_note =  ""
        self.total_price = 0
    
    #課題3_CSVから商品マスタを登録
    def registration(self):
        index = 0
        df = pd.read_csv('商品リスト.csv',header=None,encoding = "utf-8-sig")  #CSV読み込み
        print("■メニュー■")
        for num,name,price in zip(df[0],df[1],df[2]):
            if index == 0:
                index += 1
                continue
            self.item_master.append(Item(num,name,price))
            print("商品コード:{},商品名:{:　>5},価格:{}".format(num,name,price))
            index += 1
        print("")
        #課題3で不要化した
        #for menu in item_master:
            #print("商品コード:{},商品名:{:　>5},価格:{}".format(menu.item_code,menu.item_name,menu.price))

    #課題2_オーダーをコンソール（ターミナル）から登録  
    def input_order(self):
        count = 0
        while True:
            accept = int(input("購入したい商品コードを入力してください。終了したい場合は 0 を入力    "))
            if accept == 0:
                if count == 0:
                    print("またのご利用をお待ちしております。")
                    break
                else:
                    print("■ご購入品リスト■")
                    self.all("",1,0)
                    break
            else:
                count += 1
                accept_zero = str(accept).zfill(3)
                self.view(accept_zero)
    #課題6_お預かり金額、お釣り
    def deposit(self,total_price):
        deposit_money = int(input("お支払い金額を入力してください。    ")) 
        while True:
            change = deposit_money - total_price
            if change < 0:
                deposit_money = int(input("お支払い金額が不足しています。再度、お支払い金額を入力してください。    ")) 
            elif change == 0:
                print("{}円ちょうど頂きます。\n\nご購入ありがとうございました。またのご利用をお待ちしております。".format(deposit_money))
                break
            else:
                print("{}円お預かりいたします。".format(deposit_money))
                print("お釣りは{}円です。\n\nご購入ありがとうございました。またのご利用をお待ちしております。".format(change))
                break
        self.file_seve.file_write("お支払い金額：{}円".format(deposit_money))
        self.file_seve.file_write("お釣り：{}円\n\nご購入ありがとうございました。\nまたのご利用をお待ちしております。".format(change))

    #課題5_オーダーした商品の商品名、小計価格、合計金額を表示
    def all(self,note,prit_flag,subtotal):
        self.all_note += "{}\n".format(note)
        self.total_price += subtotal
        if prit_flag == 1:
            self.all_note += "合計{}円です。\n".format(self.total_price)
            print(self.all_note)
            self.file_seve.file_write("合計：{}円\n".format(self.total_price))
            self.deposit(self.total_price)

    #課題1_オーダー登録した商品名、価格を表示    
    def view(self,item_code):
        flag = 0
        total_price = 0
        for menu in self.item_master:
            if item_code == menu.item_code:
                volume = int(input("購入したい個数を入力してください。    "))   #課題4_個数の登録
                subtotal = volume * int(menu.price)
                #format {:　>3}はスペース、右埋め　>、文字数 3
                x = "商品コード:{},商品名:{:　>3},単価:{},個数:{},小計{}".format(menu.item_code,menu.item_name,menu.price,volume,subtotal)
                self.file_seve.file_write(x)
                print(x)
                self.all(x,0,subtotal)
                flag = 1
        if flag == 0:
            print("申し訳ございません商品がありません、、、（涙）") 


### メイン処理
def main():

    # オーダー登録
    order=Order()
    order.registration()#課題3_CSVから商品マスタを登録
    order.input_order() #課題2


if __name__ == "__main__":
    main()