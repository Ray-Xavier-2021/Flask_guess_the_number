from flask import Flask, render_template, request
# Import choice from random to allow a random selected choice
from random import choice
app = Flask(__name__)

# Random computer number
computer_choice = choice(range(1, 101))

@app.route('/', methods=['POST', 'GET'])
def index():
  # Get user guessed number if request method is 'POST'
  if request.method == 'POST':
    # Users guess
    guess = int(request.form['number_guess'])
    # Output message
    message = check_number_show_message(guess, computer_choice)
    print(message)


  return render_template('index.html')

# Reset function
@app.route('/reset')
def reset():
  return 'RESET PAGE'

# Create a function that compares numbers and returns according message
def check_number_show_message(guessed_number, computer_number):
  if guessed_number < computer_number:
    return f'{guessed_number} is too low'
  
  elif guessed_number > computer_number:
    return f'{guessed_number} is too high'

  else:
    
    return f'{guessed_number} is correct'


# if __name__ == '__main__':
app.run(debug=True)