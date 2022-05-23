from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

name = "Евгений"
surname = "Юрченко"
email = "eyurchenko@specialist.ru"
phone = "8-923-600-01-02"
# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 2},
#     {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
#     {"id": 4, "name": "Картофель фри", "quantity": 0},
#     {"id": 5, "name": "Кепка", "quantity": 124},
# ]


def home(request):
    return render(request,"index.html")


def item_page(request, id):
    try:
        item = Item.objects.get(pk=id)
        return render(request, "item_page.html", {"item": item})
    except ObjectDoesNotExist:
        raise Http404(f"Товар с id={id} не найден")



def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request,"items.html",context)