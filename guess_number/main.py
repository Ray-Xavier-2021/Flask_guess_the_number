from flask import Flask, render_template, request
# Import choice from random to allow a random selected choice
from random import choice

# Import 'fake' db from database
from database import db

# Create instance of app
app = Flask(__name__)

# Check if the key 'guesses' exist in database; if not create it
if 'guesses' not in db:
  db['guesses'] = []

# Check if the key 'computer_choice' exist in database; if not create it
if 'computer_choice' not in db:
  db['computer_choice'] = choice(range(1, 101))

# Random computer number
# computer_choice = choice(range(1, 101))

# test
# print(f'computer picked {computer_choice}')

# Set guesses to an empty list
# guesses = []


@app.route('/', methods=['POST', 'GET'])
def index():
  # Get user guessed number if request method is 'POST'
  if request.method == 'POST':
    # Users guess
    guess = int(request.form['number_guess'])
    # Output message
    message = check_number_show_message(guess, db['computer_choice'])
    # Append output message to  db empty guess list
    db['guesses'].append(message)

    # test
    # print(message)
    # print(db['guesses'])

  # Render template w/ guesses in reverse
  return render_template('index.html', guesses=reversed(db['guesses']))

# Reset function
@app.route('/reset')
def reset():
  # Reset computer choice and guesses list
  db['computer_choice'] = choice(range(1, 101))
  db['guesses'] = []
  return render_template('index.html', guesses=db['guesses'])

# Create a function that compares numbers and returns according message
'''
It will take in the guessed number and the computer number 
2 arguments

>>> check_number_show_message(guessed_number=5, computer_number=10)
  '5 is too low

'''
def check_number_show_message(guessed_number, computer_number):
  if guessed_number < computer_number:
    return f'{guessed_number} is too low'
  
  elif guessed_number > computer_number:
    return f'{guessed_number} is too high'

  else:
    
    return f'{guessed_number} is correct'

# Replit server config
# app.run(host-'0.0.0.0', port=81)

# Local Machine
app.run(debug=True)