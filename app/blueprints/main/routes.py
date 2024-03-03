from . import main
from flask import render_template, request, flash, url_for,  redirect
import requests
from .forms import PokemonForm, BattleForm
from  app.models import Pokemon, db, User, My_Pokemon 

from flask_login import current_user, login_required


@main.route("/")
def home():
    return render_template('home.html')

@main.route('/user/<name>')
def user(name):
    return f'hello {name}'





def get_pokemon_data(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    output=[]
    if response.ok:
        data = response.json()
        return {
            'name': data['name'].capitalize(),
            'hp': data['stats'][0]['base_stat'],
            'defense': data['stats'][3]['base_stat'],
            'attack': data['stats'][1]['base_stat'],
            'sprite': data['sprites']['front_shiny'],
            'ability': data['abilities'][0]['ability']['name']
        }
    else:
        return output.append
pokemon_names = ['charizard', 'pikachu', 'squirtle', 'bulbasaur', 'charmander', 'raichu']

@main.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    form = PokemonForm()
    if request.method == 'POST' and form.validate_on_submit:
        pokemon_identifier = form.name_or_id.data
        print(pokemon_identifier)
        pokemons = get_pokemon_data(pokemon_identifier)
        return render_template('pokemon.html', pokemons=pokemons, form=form)
    else:
        return render_template('pokemon.html', form=form)