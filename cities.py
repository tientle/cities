from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

cities_list = convert_to_dict('cities.csv')

pairs_list = []
for city in cities_list:
    pairs_list.append( (city['2019-Rank'], city['City']) )

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list)

@app.route('/city/<rank>')
def city(rank):
    city = cities_list[int(rank) - 1 ]
    return render_template('city.html', city=city)


if __name__ == '__main__':
    app.run(debug=True)
