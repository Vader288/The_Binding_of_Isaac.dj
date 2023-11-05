from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def category(request):
    return render(request, 'humster/umber1.html')


def kub(request):
    return render(request, 'humster/kub.html')

def category_1(request):
    return HttpResponse('<h1>Предсказния The Binding of Isaac: Repentance</p></h1>')

def category_2(request, cat_id):
    dict = {
        1: '<h1> Не смотри так, у других тоже есть проблемы </p></h1>',
        2: '<h1> Дьявол скрытен </p></h1>',
        3: '<h1> Ты всегда витаешь в облаках </p></h1>',
        4: '<h1> Никто не понимает, с какими проблемами ты столкнулся </p></h1>',
        5: '<h1> Висельник не принесёт тебе удачи сегодня </p></h1>',
        6: '<h1> Ты делаешь ошибки, это нормально </p></h1>',
        7: '<h1> Твоя принцесса в другом замке </p></h1>',
        8: '<h1> Почему ты такой грустный? </p></h1>',
        9: '<h1> Ты умрёшь </p></h1>',
        10: '<h1> Когда жизнь даёт тебе лимоны — меняй! </p></h1>'



    }
    if cat_id > 10:
        return redirect('/', permanent = True)

    if (cat_id >= 1):
        return HttpResponse(f'<h1></h1> <p>{dict[cat_id]}</p><p> Предсказание  {cat_id}</p> ')
    elif (cat_id == 2):
        return HttpResponse(f'<h1></h1> <p>{dict[cat_id]}</p><p> Предсказание  {cat_id}</p> ')
    elif (cat_id == 3):
        return HttpResponse(f'<h1></h1> <p>{dict[cat_id]}</p><p> Предсказание  {cat_id}</p> ')
    return HttpResponse(f'<h1></h1> <p> Девизы Warhammer40000 номер  {cat_id}</p> ' )

def category_3(request):
    return HttpResponse('</h1>ВСЁ ПОЛУЧИТСЯ!!!</p></h1>')


def category_slug(request, cat_slug):
    return HttpResponse(f'</h1>Пока это всё</p></h1> Категория -<b> {cat_slug}</p>')


def category_4(request):
    return render(request, 'humster/umber2.html')
















