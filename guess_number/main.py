from flask import Flask, render_template, request
# Import choice from random to allow a random selected choice
from random import choice
app = Flask(__name__)

# Random computer number
computer_choice = choice(range(1, 101))

# test
print(f'computer picked {computer_choice}')

# Set guesses to an empty list
guesses = []


@app.route('/', methods=['POST', 'GET'])
def index():
  # Get user guessed number if request method is 'POST'
  if request.method == 'POST':
    # Users guess
    guess = int(request.form['number_guess'])
    # Output message
    message = check_number_show_message(guess, computer_choice)
    # Append output message to empty guess list
    guesses.append(message)
    # test
    print(message)
    print(guesses)

  # Render template w/ guesses in reverse
  return render_template('index.html', guesses=reversed(guesses))

# Reset function
@app.route('/reset')
def reset():
  # Reset computer choice and guesses list
  computer_choice = choice(range(1, 101))
  guesses = []
  return render_template('index.html', guesses=reversed(guesses))

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


# if __name__ == '__main__':
app.run(debug=True)