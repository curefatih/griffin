from datetime import datetime
from app.models.reaction import Reaction
from settings import ALLOWED_EMOJIS


class VoteService:
    def __init__(self):
        self.test = None

    @staticmethod
    def add_vote(data):
        if not data['event'].get('item_user'):
            return True

        if data['event'].get('user') == data['event'].get('item_user'):
            return True

        if data['event'].get('reaction') not in ALLOWED_EMOJIS:
            return True

        reaction = Reaction()
        reaction.token = data.get('token')
        reaction.team_id = data.get('team_id')
        reaction.app_id = data.get('api_app_id')
        reaction.event_id = data.get('event_id')
        reaction.voteder = data['event'].get('user')
        reaction.rateder = data['event'].get('item_user')
        reaction.event = data['event'].get('reaction')
        reaction.channel = data['event']['item'].get('channel')
        reaction.event_datetime = datetime.fromtimestamp(data.get('event_time'))

        reaction.save()

        return True

    @staticmethod
    def remove_vote(data):
        if data['event'].get('reaction') not in ALLOWED_EMOJIS:
            return True

        rateder = data['event'].get('item_user')
        voteder = data['event'].get('user')

        event = Reaction.query.filter_by(rateder=rateder).filter_by(voteder=voteder).first()

        if event:
            event.destroy()

        return True
