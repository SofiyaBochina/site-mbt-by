from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    goods = [
        {
            "image": '/static/images/dishwasher.png',
            "title": 'Ремонт посудомоечных машин',
            "price": "80р"
        },
        {
            "image": '/static/images/washer.png',
            "title": 'Ремонт стиральных машин',
            "price": "80р"
        },
        {
            "image": '/static/images/hob.png',
            "title": 'Ремонт электрических и газовых варочных поверхностей',
            "price": "60р"
        },
        {
            "image": '/static/images/electric-kitchen.jpg',
            "title": 'Ремонт духовых шкафов',
            "price": "60р"
        },
        {
            "image": '/static/images/cooker.png',
            "title": 'Ремонт электрических и газовых плит',
            "price": "100р"
        },
        {
            "image": '/static/images/dry.png',
            "title": 'Ремонт сушильных машин',
            "price": "120р"
        },
        {
            "image": '/static/images/microwave.png',
            "title": 'Ремонт СВЧ',
            "price": "60р"
        },
    ]
    return render_template('index.html', goods=goods)


if __name__ == '__main__':
    app.run(debug=True)
