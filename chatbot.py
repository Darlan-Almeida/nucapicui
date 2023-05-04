from flask import Flask , request, jsonify
from datetime import date


app = Flask(__name__)


@app.route("/" , methods =['POST' , 'GET'])
def webhook():
  data = request.get_json(silent=True)
  print(data)
  if request.method == 'GET':
    return "manda uma mensagem"
  elif request.method == 'POST':
    playload = request.json
    date_birth = (playload['queryResult'] ['queryText'])
    if date_birth != '' :
      try:
        date_birth_string = date_birth.split('/' , 3)
        date_birth_day = date_birth_string[0]
        date_birth_day_converted = int(date_birth_day)
        date_birth_month = date_birth_string[1]
        date_birth_month_converted = int(date_birth_month)
        date_birth_year = date_birth_string[2]
        date_birth_year_converted = int(date_birth_year)   
        today = date.today() 
        age = today.year - date_birth_year_converted - ((today.month, today.day) < (date_birth_month_converted, date_birth_day_converted))
        if age >= 18 or age < 12:
          data["fulfillmentText"] = 'Infelizmente você não pode participar.O NUCA é para, apenas, adolescentes a partir de 12 anos. Se você conhece alguém que tenha interesse em participar, avise a essa pessoa! '
        else:
          data["fulfillmentText"] = 'Você está na faixa étaria do NUCA, caso queira participar entre em contato com a mobilizadora: (83) 98132-5275'
        return jsonify(data)
      except:
        data["fulfillmentText"] = 'Coloque a data nesse formato DD/MM/AA, por exemplo, 13/12/2013'
        return jsonify(data)

    

if __name__ == "__main__":
  app.run(host= '0.0.0.0', port = 8080)
  app.run(debug = True)
  print('servidor rodando')
