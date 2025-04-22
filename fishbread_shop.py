while True:

    stock = {
        "팥붕어빵": 2,
        "슈크림붕어 빵": 3,
        "초코붕어": 5
    }

    sales = {
        "팥붕어빵": 0,
        "슈크림붕어 빵": 0,
        "초코붕어": 0
    }

    def order_bread():
        while True:
            bread_type = input("주문할 빵 종류를 입력하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵, 종료): ")
            if bread_type == "종료":
                print("프로그램을 종료합니다.")
                break
            if bread_type in stock:
                bread_count = int(input("주문할 빵 개수를 입력하세요: "))
                if stock[bread_type] >= bread_count:
                    stock[bread_type] -= bread_count
                    sales[bread_type] += bread_count
                    print(f"{bread_count}개가 판매되었습니다.")
                else:
                    print(f"재고가 부족합니다. 현재 재고: {stock[bread_type]}개")
            else:
                print(f"{bread_type}는(은) 존재하지 않는 빵입니다. 다시 입력하세요.")

    while True:
        mode = input("Select mode (1: 주문, 2: 관리자, 3: 종료): ")
        if mode == "종료":
            print("프로그램을 종료합니다.")
            break
        elif mode == "주문":
            order_bread()
        elif mode == "관리자":
            admin_mode = input("관리자 모드 선택 (1: 재고 확인, 2: 판매 확인): ")