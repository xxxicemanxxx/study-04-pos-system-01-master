### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master

    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        #課題1_オーダー登録した商品名、価格を表示
        
    def view(self,item_code):
        for menu in self.item_master:
            if item_code==menu.item_code:
                #format {:　>3}はスペース、右埋め　>、文字数 3
                print("商品コード:{},商品名:{:　>3},価格:{}".format(menu.item_code,menu.item_name,menu.price))


    
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    print("■メニュー■")
    for menu in item_master:
        print("商品コード:{},商品名:{:　>3},価格:{}".format(menu.item_code,menu.item_name,menu.price))
    print("")
    # オーダー登録
    print("オーダーした商品はこちらです")
    order=Order(item_master)
    order.view("003")
    order.view("001")
    order.view("002")

    
if __name__ == "__main__":
    main()