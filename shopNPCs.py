import items
import travel

def displayShop(shopItems):
    print(f"{'Item' :<20}{'Price' :<8}{'Amount' :<8}{'|' :<8}{'Description' :<32}")
    print(f"{"=" * 36}{'|'}{'=' * 50}")
    for item in range(len(shopItems)):
        print(f"{shopItems[item].name :<20}{'$' + str(shopItems[item].price) :<8}{shopItems[item].amount :<8}{'|' :<8}{shopItems[item].desc :<32}")

def openShop(area):
    if area == 1:
        displayShop(items.area1Items)
    elif area == 2:
        displayShop(items.area2Items)
    elif area == 3:
        displayShop(items.area3Items)
    elif area == 4:
        displayShop(items.area4Items)
    elif area == 5:
        displayShop(items.area5Items)
    elif area == 6 or area == 7 or area == 8:
        displayShop(items.area6to8Items)
    elif area == 0:
        displayShop(items.devAreaItems)

area = int(input())

openShop(area)