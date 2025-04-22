while True:
    mode = input("Select mode (1: 주문, 2: 관리자, 3: 종료): ")
    #mode = "종료"
    if mode == "종료":
        print("프로그램을 종료합니다.")
        break
    #mode = "주문":
    elif mode == "주문":
        print("주문 모드입니다.")
        while True:
            order_bread = input("주문할 메뉴를 입력하세요 (종료: '종료'): ")
            if order_bread == "종료":
                print("주문을 종료합니다.")
                break
            else:
                print(f"{order_bread}를 주문하셨습니다.")
    #mode = "관리자":
    elif mode == "관리자":
        print("관리자 모드입니다.")
        while True:
            admin_mode = input("관리자 작업을 입력하세요 (종료: '종료'): ")
            if admin_mode == "종료":
                print("관리자 작업을 종료합니다.")
                break
            else:
                print(f"{admin_mode} 작업을 수행하셨습니다.")