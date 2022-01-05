from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website.models import Note, Methane
from website import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        carbohydrates = request.form.get('carbohydrates')
        protein = request.form.get('protein')
        lipids = request.form.get('lipids')
        substrates = request.form.get('substrates')
        new_note = Note(data=note, user_id=current_user.id)
        new_methane = Methane(carbohydrates=carbohydrates, user__id=current_user.id)
        new_protein = Methane(protein=protein, user__id=current_user.id)
        new_lipids = Methane(lipids=lipids, user__id=current_user.id)
        new_substrates = Methane(substrates=substrates, user__id=current_user.id)
        db.session.add(new_note)
        db.session.add(new_methane)
        db.session.add(new_protein)
        db.session.add(new_lipids)
        db.session.add(new_substrates)
        db.session.commit()
        flash('Note added!', category='success')

    return render_template("home1.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route('/delete-methane', methods=['POST'])
def delete_methane():
    methane = json.loads(request.data)
    methaneId = methane['methaneId']
    methane = Methane.query.get(methaneId)
    if methane:
        if methane.user__id == current_user.id:
            db.session.delete(methane)
            db.session.commit()

    return jsonify({})
