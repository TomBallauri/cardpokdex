from flask import Flask, jsonify, request
from flask_cors import CORS # N'oubliez pas l'importation de CORS pour la connexion React
from flask_sqlalchemy import SQLAlchemy

# Initialiser l'application Flask
app = Flask(__name__)
# Activer CORS pour permettre les requêtes depuis React (localhost:3000)
CORS(app) 

# --- Configuration de la Base de Données (SQLite) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardpokdex.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) 
# ----------------------------------------------------

# --- Modèle de la Table 'sets' ---
class Set(db.Model):
    # La clé primaire est 'id', qui est une chaîne de caractères
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    series = db.Column(db.String(100))
    total = db.Column(db.Integer)
    releaseDate = db.Column(db.Date)
    logo = db.Column(db.String(255))

    # Relation inverse: un Set peut avoir plusieurs Cartes (Card)
    cards = db.relationship('Card', backref='set', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'series': self.series,
            'total': self.total,
            'releaseDate': str(self.releaseDate),
            'logo': self.logo
        }
    
# --- Modèle de la Table 'cards' ---
class Card(db.Model):
    # La colonne `id` de la table SQL est longue (512), on la garde ainsi
    # On ajoute une colonne id auto-incrémentée si on veut une clé primaire simple, 
    # mais ici on utilise l'ID de la carte comme clé primaire car il est unique.
    
    # ID de la carte (Clé Primaire)
    id = db.Column(db.String(512), primary_key=True) 
    name = db.Column(db.String(512))
    supertype = db.Column(db.String(512))
    types = db.Column(db.String(512))
    number = db.Column(db.Integer)
    artist = db.Column(db.String(512))
    rarity = db.Column(db.String(512))
    flavorText = db.Column(db.String(512))
    small = db.Column(db.String(512))
    large = db.Column(db.String(512))

    # Clé étrangère: relie la carte à son set (colonne 'set_id')
    set_id = db.Column(db.String(20), db.ForeignKey('set.id'), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'supertype': self.supertype,
            'types': self.types,
            'number': self.number,
            'artist': self.artist,
            'rarity': self.rarity,
            'flavorText': self.flavorText,
            'small': self.small,
            'large': self.large,
            'set_id': self.set_id
        }

# Définir votre première route API (endpoint)
@app.route('/')
def home():
    return "Bienvenue sur l'API Flask!"

# Un exemple de route que votre application React pourrait appeler
@app.route('/api/message')
def get_message():
    return jsonify({
        "message": "Ceci est un message de votre serveur Flask !"
    })

@app.route('/api/cards', methods=['GET'])
def get_all_cards():
    cards = Card.query.all()
    return jsonify([card.to_dict() for card in cards])

@app.route('/api/sets', methods=['GET'])
def get_all_sets():
    sets = Set.query.all()
    return jsonify([set_item.to_dict() for set_item in sets])

@app.route('/api/card/<string:card_id>', methods=['GET'])
def get_card_details(card_id):
    """Récupère les détails d'une carte spécifique par son ID."""
    
    # Utilise l'ID pour interroger la base de données
    card = Card.query.get(card_id)
    
    # Si la carte n'est pas trouvée, renvoie une erreur 404
    if card is None:
        return jsonify({"message": f"Carte avec l'ID {card_id} non trouvée"}), 404
        
    # Renvoie les données au format JSON
    return jsonify(card.to_dict())


@app.route('/api/search', methods=['GET'])
def search_cards():
    """Recherche basique des cartes par nom via le paramètre de query `q`.
    Renvoie une liste JSON des cartes correspondantes.
    Exemple: GET /api/search?q=pikachu
    """
    q = request.args.get('q', '').strip()
    if not q:
        return jsonify([])

    # Recherche case-insensitive dans le champ name
    try:
        results = Card.query.filter(Card.name.ilike(f"%{q}%")).all()
    except Exception:
        # En cas d'erreur (par ex. colonne manquante), renvoyer une liste vide
        results = []

    return jsonify([card.to_dict() for card in results])

@app.route('/api/set/<string:set_id>', methods=['GET'])
def get_set_details(set_id):
    """Récupère les détails d'un set spécifique par son ID."""
    
    # Utilise l'ID pour interroger la base de données
    set_item = Set.query.get(set_id)
    
    # Si le set n'est pas trouvé, renvoie une erreur 404
    if set_item is None:
        return jsonify({"message": f"Set avec l'ID {set_id} non trouvé"}), 404
        
    # Renvoie les données au format JSON
    return jsonify(set_item.to_dict())

if __name__ == '__main__':
    # Lance l'application si vous l'exécutez directement avec `python app.py`
    app.run(debug=True)