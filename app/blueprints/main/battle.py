from flask import render_template, request, jsonify
from app.models import User, Pokemon, db
from sqlalchemy.sql import func

@app.route('/battle', methods=['POST'])
def battle():
    # Assuming you're receiving the usernames of the two users battling
    user1_name = request.form.get('user1')
    user2_name = request.form.get('user2')

    user1 = User.query.filter_by(username=user1_name).first()
    user2 = User.query.filter_by(username=user2_name).first()

    if not user1 or not user2:
        return jsonify({'error': 'One or both users not found'}), 404

    # Calculate the total stats for each team
    team1_stats = sum([p.base_attack + p.base_defense + p.base_hp for p in user1.pokemons])
    team2_stats = sum([p.base_attack + p.base_defense + p.base_hp for p in user2.pokemons])

    # Determine winner based on total stats
    if team1_stats > team2_stats:
        winner = user1.username
    elif team2_stats > team1_stats:
        winner = user2.username
    else:
        winner = "It's a tie!"

    return jsonify({'winner': winner})
