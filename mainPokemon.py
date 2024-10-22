import requests
from dbActions import addPokemon, fetchFromDb

def fetch_pokemon(name):
   response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
   responseData = response.json()['species']
   print(f"{responseData['name']}")
   addPokemon(responseData)


def choose_random_pokemon():
   response = requests.get('https://pokeapi.co/api/v2/pokemon/')
   from random import randrange
   pokemon_choosen = response.json()['results'][randrange(10)]['name']
   return pokemon_choosen
   
def load_from_db():
   return fetchFromDb()
      
def find_pokemon(pokemon):
     pokemons = load_from_db()
     if pokemons:
        for i in range(len(pokemons)):
         if pokemons[i]['name'] == pokemon:
            print('pokemon already in db: ')
            print(pokemons[i]['name'])
            return
     fetch_pokemon(pokemon) 

       
      
def main():
   ans = input('would you like to draw a Pokémon? (y/n):  ')
   while ans.lower() != 'no':
    if ans.lower() == 'yes':      
      find_pokemon(choose_random_pokemon())
      ans = input('would you like to draw a Pokémon? (y/n):  ')
    else:
     print('please enter a valid answer')
     ans = input('would you like to draw a Pokémon? (y/n): ')
   print('its your loss ;)') 
   
main()



