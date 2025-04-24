from fishbread_model import Breadshop

shop = Breadshop()

while True:
    mode = input("Select mode (1: 주문, 2: 관리자, 3: 종료): ")
    if mode == "종료":
        calculate_sales()
        print("프로그램을 종료합니다.")
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
