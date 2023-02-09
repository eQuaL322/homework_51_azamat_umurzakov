import random

from django.core.handlers.wsgi import WSGIRequest


class Cat:
    name = ''
    age = 1
    happines = 0
    satiety = 0
    is_sleeping = False
    cat_mood = 'data:image/jpeg;base64,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'

    @staticmethod
    def get_name(request: WSGIRequest):
        if request.method == 'POST':
            Cat.name = request.POST.get('name')
            return Cat.name

    @staticmethod
    def cat_info(request: WSGIRequest):
        if request.method == 'POST':
            action = request.POST.get('action')
            Cat.name = request.POST.get('name')
            if action == 'feed':
                if Cat.is_sleeping:
                    pass
                else:
                    Cat.satiety += 15
                    Cat.happines += 5
                    Cat.cat_mood = 'https://media.tenor.com/Plqkx-_AJSIAAAAC/full-im-full.gif'
                    if Cat.satiety > 100:
                        Cat.satiety -= 30
                        Cat.cat_mood = 'https://www.belanta.vet/vet-blog/wp-content/uploads/2018/07/pochechnaya-nedostatochnost-u-koshek_01.jpg'
                    if Cat.happines > 100:
                        Cat.happines = 100
            elif action == 'play':
                if Cat.is_sleeping:
                    Cat.is_sleeping = False
                    Cat.happines -= 5
                    if Cat.happines < 0:
                        Cat.happines = 0
                else:
                    anger_chance = random.randint(1, 3)
                    if anger_chance == 1:
                        Cat.happines = 0
                        Cat.cat_mood = 'https://sun9-71.userapi.com/impg/CfACvV_HMRk_o7LNLc3bT19xd--Ht4Sna7SHnw/y6hDGi5RDPk.jpg?size=640x400&quality=96&sign=4bda639708a2c472fabff59eb47a1265&c_uniq_tag=AiT49Z4LNoATnhnR9p5gLj_PCRM1RcvebrUwNMgCaiA&type=album'
                    else:
                        Cat.satiety -= 10
                        Cat.happines += 15
                        Cat.cat_mood = 'https://www.petmd.com/sites/default/files/cat-moods-playful-cat.jpg'
                        if Cat.satiety < 0:
                            Cat.satiety = 0
                        if Cat.happines > 100:
                            Cat.happines = 100
            elif action == 'sleep':
                Cat.is_sleeping = True
                Cat.cat_mood = 'https://www.petmd.com/sites/default/files/cat-moods-relaxed-cat_0.jpg'
