from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    goods = [
        {
            "image": '/static/images/good-dishwasher.webp',
            "title": 'Ремонт посудомоечных машин',
            "price": "80р",
            "alt": 'Фотография посудомоечной машины',
            "info": [
                'замена циркуляционного насоса',
                'ремонт системы аквастоп',
                'ремонт системы слива',
                'ремонт электронного модуля',
                'замена сливного насоса',
                'обновление ПО (программного обеспечения)',
                'замена шланга аквастоп',
                'ремонт прочих неисправностей'
            ]
        },
        {
            "image": '/static/images/good-washer.jpeg',
            "title": 'Ремонт стиральных машин',
            "price": "80р",
            "alt": 'Фотография стиральной машины',
            "info": [
                'ремонт электронного модуля',
                'замена подшипника барабана',
                'ремонт системы сушки стиральной-сушильной машины',
                'замена сливного насоса',
                'замена нагревателя (ТЭНа)',
                'извлечение посторонних предметов',
                'замена амортизаторов',
                'ремонт прочих неисправностей'
            ]
        },
        {
            "image": '/static/images/good-dry.jpg',
            "title": 'Ремонт сушильных машин',
            "price": "120р",
            "alt": 'Фотография сушильной машины',
            "info": [
                'ремонт электронного модуля',
                'замена нагревателя (ТЭНа)',
                'замена барабана',
                'замена ремня',
                'ремонт системы теплового насоса',
                'замена роликов барабана',
                'ремонт прочих неисправностей'
            ]
        },
        {
            "image": '/static/images/good-electric-kitchen.jpg',
            "title": 'Ремонт духовых шкафов',
            "price": "60р",
            "alt": 'Фотография духового шкафа',
            "info": [
                'ремонт электронного модуля',
                'ремонт таймера',
                'замена нагревательного элемента (ТЭНа)',
                'ремонт электропроводки',
                'замена плафона (лампы подсветки)',
                'замена терморегулятора (термостата)',
                'ремонт прочих неисправностей'
            ]
        },
        {
            "image": '/static/images/good-cooker.jpg',
            "title": 'Ремонт электрических и газовых плит',
            "price": "100р",
            "alt": 'Фотография плиты',
            "info": [
                'замена конфорок',
                'замена энергорегулятора (переключателя режимов)',
                'ремонт системы газ-контроль',
                'ремонт электронного модуля',
                'ремонт электропроводки',
                'замена терморегулятора (термостата)',
                'ремонт прочих неисправностей'
            ]
        },
        {
            "image": '/static/images/good-microwave.jpg',
            "title": 'Ремонт СВЧ (микроволновок)',
            "price": "60р",
            "alt": 'Фотография микроволновки',
            "info": [
                'ремонт электронного модуля',
                'замена изолятора (слюды)',
                'замена магнитрона',
                'замена мотора тарелки',
                'ремонт привода открытия двери (в СВЧ с автоматическим открытием двери)',
                'ремонт прочих неисправностей'
            ]
        },
        {
            "image": '/static/images/good-hob.webp',
            "title": 'Ремонт электрических и газовых варочных поверхностей',
            "price": "60р",
            "alt": 'Фотография четырех видов варочных поверхностей',
            "info": [
                'ремонт электронного модуля',
                'замена конфорок',
                'замена энергорегулятора (переключателя режимов)',
                'ремонт системы газ-контроль',
                'ремонт электроподжига',
                'ремонт прочих неисправностей'
            ]
        },
    ]
    brands = [
        {
            "image": '/static/images/brand-bosch.svg',
            "name": 'bosch',
            'type': 'contain'
        },
        {
            "image": '/static/images/brand-siemens.svg',
            "name": 'siemens',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-neff.svg',
            "name": 'neff',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-gorenje.svg',
            "name": 'gorenje',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-smeg.svg',
            "name": 'smeg',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-gaggenau.svg',
            "name": 'gaggenau',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-zanussi.svg',
            "name": 'zanussi',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-samsung.svg',
            "name": 'samsung',
            'type': 'contain'
        },
        {
            "image": '/static/images/brand-lg.svg',
            "name": 'lg',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-ariston.svg',
            "name": 'ariston',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-indesit.svg',
            "name": 'indesit',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-candy.svg',
            "name": 'candy',
            'type': 'contain'
        },
        {
            "image": '/static/images/brand-newbeko.svg',
            "name": 'newbeko',
            'type': 'contain'
        },
        {
            "image": '/static/images/brand-daewoo.svg',
            "name": 'daewoo',
            'type': 'cover'
        },
        {
            "image": '/static/images/brand-aeg.svg',
            "name": 'aeg',
            'type': 'contain'
        },
        {
            "image": '/static/images/brand-electrolux.svg',
            "name": 'electrolux',
            'type': 'contain'
        },
    ]
    return render_template('index.html', goods=goods, brands=brands)


if __name__ == '__main__':
    app.run(debug=True)
