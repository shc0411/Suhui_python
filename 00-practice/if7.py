# 실습: 단일 if문으로 파스타 조합 완성하기

# 고춧가루, 베이컨, 랍스터 추가 여부를 입력받아 파스타 조합을 완성하시오
# 원하는 재료만 추가하고, 마지막에 최종 조합을 출력하시오

pepper = input("고춧가루를 추가할까요? (y/n): ")
niku = input("베이컨을 추가할까요? (y/n): ")
lobster = input("랍스터를 추가할까요? (y/n): ")

pasta = "기본 파스타"

if pepper == "y":
    pasta = pasta + " + 고춧가루"

if niku == "y":
    pasta = pasta + " + 베이컨"

if lobster == "y":
    pasta = pasta + " + 랍스터"

print("최종 조합: ", pasta)