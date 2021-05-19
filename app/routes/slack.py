from flask import Blueprint, current_app
from slackeventsapi import SlackEventAdapter

from app.services.vote import VoteService

slack_events = Blueprint('slack_events', __name__)
slack_events_adapter = SlackEventAdapter(current_app.config['SLACK_SIGNING_TOKEN'], "/slack/events", slack_events)


@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    print(event_data)
    service = VoteService()
    service.add_vote(event_data)

    return 'Ok\n'


@slack_events_adapter.on("reaction_removed")
def reaction_removed(event_data):
    service = VoteService()
    service.remove_vote(event_data)

    return 'Ok\n'
