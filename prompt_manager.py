prompts = []

def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목을 입력해야 합니다.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용을 입력해야 합니다.")

    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    while True:
        print("\n카테고리 선택:")
        for i, cat in enumerate(categories, 1):
            print(f"{i}) {cat}")
        
        choice = input("선택: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            selected_category = categories[int(choice) - 1]
            break
        print("잘못된 선택입니다. 다시 선택해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": selected_category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print("\n프롬프트가 추가되었습니다!")

def main_menu():
    while True:
        print("\n=== 나만의 프롬프트 관리 ===")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 목록")
        print("3. 카테고리별 조회")
        print("4. 프롬프트 검색")
        print("5. 프롬프트 상세 보기")
        print("6. 즐겨찾기 관리")
        print("7. 즐겨찾기 목록")
        print("0. 종료")
        
        choice = input("선택: ").strip()
        
        if choice == '1':
            add_prompt()
        elif choice == '0':
            print("종료합니다.")
            break
        elif choice in ['2', '3', '4', '5', '6', '7']:
            print(f"{choice}번 메뉴는 아직 구현되지 않았습니다.")
        else:
            print("잘못된 선택입니다. 0~7 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main_menu()
