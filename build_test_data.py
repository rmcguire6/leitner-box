import os
from app import db
from app import models

USERS = [
  {'username' :"Rogan", "cards_per_day": 5},
  {'username' :"Forrest", "cards_per_day": 4},
  {'username' :"Hiram", "cards_per_day": 3},
  {'username' :"David", "cards_per_day": 5},
  {'username' :"Rebecca", "cards_per_day": 2}
]

CARDS = [
  {'subject': 'nec', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 4},
  {'subject': 'eu', 'question': "eu tellus eu augue porttitor interdum. Sed",
  'answer':"in aliquet lobortis, nisi nibh", 'active': True, 'user_id': 3},
  {'subject': 'auctor', 'question': "augue ut lacus. Nulla tincidunt, neque",
   'answer':"at auctor ullam corper, nisl arcu", 'active': True, 'user_id': 2},
  {'subject': 'libero', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 1},
  {'subject': 'tristique', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 5},
  {'subject': 'nec', 'question': "libero lacus, varius", 'answer':"ac risus.",
  'active': True, 'user_id': 4},
  {'subject': 'eu', 'question': "eu tellus eu augue porttitor interdum. Sed",
   'answer':"in aliquet lobortis, nisi nibh", 'active': True, 'user_id': 3},
  {'subject': 'auctor', 'question': "augue ut lacus. Nulla tincidunt, neque",
  'answer':"at auctor ullam corper, nisl arcu", 'active': True, 'user_id': 2},
  {'subject': 'libero', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 1},
  {'subject': 'tristique', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 5},
  {'subject': 'nec', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 4},
  {'subject': 'eu', 'question': "eu tellus eu augue porttitor interdum. Sed",
   'answer':"in aliquet lobortis, nisi nibh", 'active': True, 'user_id': 3},
  {'subject': 'auctor', 'question': "augue ut lacus. Nulla tincidunt, neque",
   'answer':"at auctor ullam corper, nisl arcu", 'active': True, 'user_id': 2},
  {'subject': 'libero', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 1},
  {'subject': 'tristique', 'question': "libero lacus, varius", 'answer':"ac risus.",
   'active': True, 'user_id': 5}
]

if os.path.exists('lebox.db'):
    os.remove('lebox.db')

db.create_all()

for card in CARDS:
    c = models.Card(subject=card['subject'], question=card['question'],
        answer=card['answer'], active=card['active'], user_id=card['user_id'])
    db.session.add(c)
db.session.commit()

for user in USERS:
    u = models.User(username=user['username'], cards_per_day=user['cards_per_day'])
    db.session.add(u)
db.session.commit()
