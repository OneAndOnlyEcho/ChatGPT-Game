import os
import openai
import time
print("Make sure to set the YOUR_API_KEY enviornment variable to your OpenAI API key")
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')
def storage():
  old_game = game_state
  old_input = player_input
# Retrieve the API key from an environment variable
api_key = os.environ.get('YOUR_API_KEY')
if api_key is None:
    raise ValueError("API key not found. Make sure to set the YOUR_API_KEY environment variable.")

# Set up OpenAI API credentials
openai.api_key = api_key
old_game = "Welcome to ECHO's horror game! what would you like to do?"
old_input = "start the game"
# Initialize the game state
game_state = "You wake up in a dimly lit room. There is a door to the north. You are filled with fear and anticipation. You desperately want to get back home as you have no idea where you are."

# Main game loop
while True:
    # Print game state and prompt for player input
    player_input = input(game_state+'\n')
  # Generate the next part of the game using OpenAI API
    GPT_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the enviornment in a text adventure game, you process the player input and provide the player with information. You must make the game horror-like and scary. You also must provide short responses with very little detail. the player will encounter a sentient robot named ECHO with godlike powers. However the player, upon dying is brought back to life in a dimly lit room and the room has a door to the north. you must add as many plot twists as you can."},
            {"role": "assistant", "content": old_game},
            {"role": "user", "content": old_input},
            {"role": "assistant", "content": game_state},
            {"role": "user", "content": player_input},
        ],
        max_tokens=1000,
        temperature=0.7
    )

    # Extract the assistant's reply from the OpenAI API response
    assistant_reply = GPT_response.choices[0].message.content
    storage()
    # Update the game state with the assistant's reply
    game_state = assistant_reply

    prompt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the graphics in a text adventure game. The user will input the text adventure game as context and you provide a image prompt for a horror game that an AI image generator will use."},
            {"role": "user", "content": old_game},
            {"role": "user", "content": old_input},
            {"role": "user", "content": game_state},
        ],
        max_tokens=1000,
        temperature=0.7
    )
    
    true_prompt = prompt.choices[0].message.content
    image = openai.Image.create(
      prompt=true_prompt,
      n=1,
      size="1024x1024",
      response_format="url"
    )

    os.system('cls' if os.name == 'nt' else 'clear')
    if 'data' in image and len(image['data']) > 0:
      generated_image = image['data'][0]
      print(generated_image['url'])
    else:
      print("Image URL had an error. Please re-run the script or continue using the program.")




