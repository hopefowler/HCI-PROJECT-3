#!/usr/bin/env python3
"""A simple chatbot (that serves as a RA) that guides students in a fridge situation with their roommate."""

from chatbot import ChatBot


class OxyCSBot(ChatBot):
    """A simple chatbot that directs students to office hours of CS professors."""

    STATES = [
        'waiting',
        'space_imbalance'
        'smelly'
        'stealing_food'
        'food_constraints'
    
        'no',
        'receptive',
        'nonreceptive',
        'unknown',

        'RA_help'
        'scared'
        'bad_response'
        'incompatible'
        
        'rant'
        'advice'
        'solution'
        'room_change'
        
        'personal_issue'
        'roommate_issue'
    ]

    TAGS = {
        # fridge issue
        'space imbalance': 'space_imbalance',
        'space':'space_imbalance',
        'not enough':'space_imbalance',
        'room': 'space_imbalance',
        'my shelf':'space_imbalance',


        'smelly':'smelly',
        'smell':'smelly',
        'gross':'smelly',
        'fishy':'smelly',
        'stinky':'smelly',
        'reek':'smelly',
        'pungent':'smelly',
        'stank':'smelly',

       'stealing food': 'stealing_food',
        'steal':'stealing_food',
        'taking food':'stealing_food',
        'taking my food':'stealing_food',
        'eating my food':'stealing_food',
        'secretly':'stealing_food',
        'stealing': 'stealing_food',

        'food constraints':'food_constraints',
        'allergies':'food_constraints',
        'allergy':'food_constraints',
        'vegetarian':'food_constraints',
        'pescatarian':'food_constraints',
        'vegan':'food_constraints',
        'gluten free':'food_constraints',
        'GF':'food_constraints',
        'dairy free':'food_constraints',
        'meat':'food_constraints',
        'beef':'food_constraints',
        'religion':'food_constraints',
        'religious':'food_constraints',

        #conversation response
        'no': 'no',
        'nope': 'no',
        'nah': 'no',

       'yes':'receptive',
        'receptive':'receptive',
        'went well':'receptive',
        'was good':'receptive',
        'yes and yes':'receptive',

        'nonreceptive':'nonreceptive',
        'not receptive':'nonreceptive',
        'yes and no':'nonreceptive',
        'yes but no':'nonreceptive',
        'went badly':'nonreceptive',
        'went poorly':'nonreceptive',
        'not go well':'nonreceptive',

        #reasoning
        'your help':'RA_help',
        'RA help':'RA_help',
        'run it by you':'RA_help',
        'run it by':'RA_help',
        'talk to you':'RA_help',
        'RA':'RA_help',
        'help':'RA_help',

        'scared':'scared',
        'scary':'scared',
        'anxious':'scared',
        'anxiety':'scared',
        'nervous':'scared',
        'bitch':'scared',
        'terrifying':'scared',
        'terrified':'scared',
        'frightened':'scared',
        'afraid':'scared',
        'panic':'scared',
        'worried':'scared',

        'ignored':'bad_response',
        'ignoring':'bad_response',
        'angry':'bad_response',
        'mad':'bad_response',
        'yelled':'bad_response',
        'screamed':'bad_response',
        'not care':'bad_response',
        'aggressive':'bad_response',
        'crying':'bad_response',
        'cried':'bad_response',
        'change':'bad_response',
        'unwilling':'bad_response',
        'budge':'bad_response',
        'scary':'bad_response',
        'mean':'bad_response',

        'habit': 'incompatible',
        'habits':'incompatible',
        'incompatible': 'incompatible',
        'not compatible': 'incompatible',
        'incompatability': 'incompatible',
        'lifestyle': 'incompatible',
        'differences': 'incompatible',
        'different': 'incompatible',

        #what are you looking for?
        'rant':'rant',
        'complain':'rant',
        'ranting':'rant',
        'complaining':'rant',

        'advice':'advice',
        'guidance':'advice',
        'advising':'advice',
        'help':'advice',
        'how to':'advice',

        'solution':'solution',
        'solutions':'solution',
        'solve':'solution',
        'suggestions':'solution',
        'ideas':'solution',
        'pointers':'solution',
        'tips':'solution',
        'suggestion':'solution',
        'idea':'solution',
        'pointer':'solution',

        'room change':'room_change',
        'move out':'room_change',
        'leave':'room_change',
        'switch':'room_change',
        'new room':'room_change',
        'new roommate':'room_change',
        'different roommate':'room_change',
        'different room':'room_change',
        'change':'room_change',
        'change rooms':'room_change',
        'get out':'room_change',
        'REHS':'room_change',
        'housing':'room_change',

        'personal issue': 'personal_issue',
        'personal': 'personal_issue',
        'myself':'personal_issue',
        'self':'personal_issue',

        'roommate issue': 'roommate_issue',
        'roommate':'roommate_issue',
        'them':'roommate_issue',
        'their':'roommate_issue',


        #generic
        'thanks': 'thanks',
        'okay': 'success',
        'bye': 'success',
        'yes': 'yes',
        'yep': 'yes',
        'no': 'no',
        'nope': 'no',
    }

    FRIDGE_ISSUE =  [
        'space_imbalance',
        'smelly',
        'stealing_food',
        'food_constraints',
    ]

    CONVERSATION_RESPONSE =[
        'no',
        'receptive',
        'nonreceptive',
    ]

    REASONING =[
        'RA_help',
        'scared',
        'bad_response',
        'incompatible',
        'no',
        'yes'
    ]

    LOOKING_FOR =[
        'rant',
        'advice',
        'solution',
        'room_change',
        'roommate_issue',
        'personal_issue',
    ]

        
    def __init__(self):
        """Initialize the OxyCSBot.

        The `professor` member variable stores whether the target professor has
        been identified.
        """
        super().__init__(default_state='waiting')
        self.fridge_issue = None
        self.conversation_response = None
        self.reasoning = None
        self.looking_for = None

    def get_fridge_issue(self, fridge_issue):
        """Find the  of a professor.

        Arguments:
            professor (str): The professor of interest.

        Returns:
            str: The office hours of that professor.
        """

        responses = {
            'space_imbalance': 'I am so sorry that there is not an even sharing of the fridge.'
                               'That must be so frustrating! ',
            'smelly': 'GROSS! I am SO sorry that your communal fridge does not smell good.',
            'stealing_food': 'Oh. my. god. THIEF! That is NOT okay. ',
            'food_constraints': 'Oh no! How inconsiderate! Your restrictions are valid!',

        }
        return responses[fridge_issue]


    def get_conversation_response(self, conversation_response):

        responses = {
            'no': 'Why not?',
            'receptive': 'Has this problem come up again since your first conversation?',
            'nonreceptive': 'I am glad you took that step! What makes you think it did not go well?',

        }
        return responses[conversation_response]


    def get_reasoning(self, reasoning):

        responses = {
            'RA_help': 'Would you like to rant or are you seeking advice?',
            'scared': 'What makes you feel that way? Is it a personal issue or a roommate issue?',
            'bad_response': 'What are you looking for from me?',
            'incompatible': 'How can I best help you with this?',
            'no': 'Seems like you got it all figured out, stop wasting my time haha',
            'yes': 'What are you looking for from me?',

        }
        return responses[reasoning]

    def get_looking_for(self, looking_for):

        responses = {
            'rant': 'I am here to listen!',
            'advice': 'Here are some tips on how to have healthy conversations with roommates!'
                      'I recommend the LARA method: L is for LISTENING (make sure to ACTIVELY listen which means'
                      'nodding and maintaining eye contact to physically show that you are listening!)'
                      'A stands for AFFIRM and acknowledge (Let them know that their feelings are valid!)'
                      'R stands for RESPOND (Once you acknowledge their POV, make sure to respond respectfully'
                      'and finally, A stands for ADD (This is when either of you can add to the conversation '
                      'to work towards a solution together!'
                      'Try it out, and let me know how it goes!',
            'solution': 'Here are some things that have worked in the past:'
                        'Try having the conversation one more time and look to find a compromise.'
                        'Try labeling your tupperware and dividing up the shelves.'
                        'And worst case scenario, there is always a communal fridge in each residential hall'
                        'Hope that helps!',
            'room_change': 'I am sorry that your roommate situation has got this bad. Here is the ResED contact info'
                            'which you can use to request a room change.'
                           'resed@oxy.edu',
            'personal_issue': 'I understand that it can be really scary and difficult to have these conversations,'
                              'but college is a time to learn how to navigate these relationships, and'
                              'I encourage you to got outside your comfort zone to talk to them. If you are really'
                              'struggling with this, I encourage you to go to Emmons counseling for free sessions'
                              'to help your personal growth!',
            'roommate_issue': 'I am sorry things have become so difficult with your roommate. They seem'
                              'really hard to live with it.Here is the ResED contact info'
                            'which you can use to request a room change.: resed@oxy.edu',


        }
        return responses[looking_for]

    # "waiting" state functions

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        self.fridge_issue = None
        if 'space_imbalance' in tags:
            for fridge_issue in self.FRIDGE_ISSUE:
                if fridge_issue in tags:
                    self.fridge_issue = fridge_issue
                    return self.go_to_state('space_imbalance')
        elif 'smelly' in tags:
            for fridge_issue in self.FRIDGE_ISSUE:
                if fridge_issue in tags:
                    self.fridge_issue = fridge_issue
                    return self.go_to_state('smelly')
        elif 'stealing_food' in tags:
            for fridge_issue in self.FRIDGE_ISSUE:
                if fridge_issue in tags:
                    self.fridge_issue = fridge_issue
                    return self.go_to_state('stealing_food')
        elif 'food_constraints' in tags:
            for fridge_issue in self.FRIDGE_ISSUE:
                if fridge_issue in tags:
                    self.fridge_issue = fridge_issue
                    return self.go_to_state('food_constraints')
        else:
            return self.finish('confused')


    # fridge issue state functions

    def on_enter_fridge_issue(self):
        """Send a message when entering the "fridge_issue" state."""
        response = [self.get_fridge_issue(self.fridge_issue),
                    'Have you had a conversation about this with your roommate and did it go well?']
        return response

    def respond_from_fridge_issue(self, message, tags):
        self.conversation_response = None
        if 'no' in tags:
            for conversation_response in self.CONVERSATION_RESPONSE:
                if conversation_response in tags:
                    self.conversation_response = conversation_response
                    return self.go_to_state('no')
        elif 'receptive' in tags:
            for conversation_response in self.CONVERSATION_RESPONSE:
                if conversation_response in tags:
                    self.conversation_response = conversation_response
                    return self.go_to_state('receptive')
        elif 'nonreceptive' in tags:
            for conversation_response in self.CONVERSATION_RESPONSE:
                if conversation_response in tags:
                    self.conversation_response = conversation_response
                    return self.go_to_state('nonreceptive')
        else:
            return self.finish('confused')


    # conversation response state functions

    def on_enter_convo_response(self):
        response = [self.get_conversation_response(self.conversation_response)]

        return response


    def respond_from_convo_response(self, message, tags):
        self.reasoning = None
        if 'RA_help' in tags:
            for reasoning in self.REASONING:
                if reasoning in tags:
                    self.reasoning = reasoning
                    return self.go_to_state('RA_help')
        elif 'scared' in tags:
            for reasoning in self.REASONING:
                if reasoning in tags:
                    self.reasoning = reasoning
                    return self.go_to_state('scared')
        elif 'bad_response' in tags:
            for reasoning in self.REASONING:
                if reasoning in tags:
                    self.reasoning = reasoning
                    return self.go_to_state('bad_response')
        elif 'incompatible' in tags:
            for reasoning in self.REASONING:
                if reasoning in tags:
                    self.reasoning = reasoning
                    return self.go_to_state('incompatible')
        elif 'no' in tags:
            for reasoning in self.REASONING:
                if reasoning in tags:
                    self.reasoning = reasoning
                    return self.go_to_state('no')
        elif 'yes' in tags:
            for reasoning in self.REASONING:
                if reasoning in tags:
                    self.reasoning = reasoning
                    return self.go_to_state('yes')
        else:
            return self.finish('confused')


    # reasoning state functions

    def on_enter_reasoning(self):
        response = [self.get_reasoning(self.reasoning)]

        return response

    def respond_from_reasoning(self, message, tags):
        self.looking_for = None
        if 'rant' in tags:
            for looking_for in self.LOOKING_FOR:
                if looking_for in tags:
                    self.looking_for = looking_for
                    return self.go_to_state('rant')
        elif 'advice' in tags:
            for looking_for in self.LOOKING_FOR:
                if looking_for in tags:
                    self.looking_for = looking_for
                    return self.go_to_state('advice')
        elif 'solution' in tags:
            for looking_for in self.LOOKING_FOR:
                if looking_for in tags:
                    self.looking_for = looking_for
                    return self.go_to_state('solution')
        elif 'room_change' in tags:
            for looking_for in self.LOOKING_FOR:
                if looking_for in tags:
                    self.looking_for = looking_for
                    return self.go_to_state('room_change')
        elif 'roommate_issue' in tags:
            for looking_for in self.LOOKING_FOR:
                if looking_for in tags:
                    self.looking_for = looking_for
                    return self.go_to_state('roommate_issue')
        elif 'personal_issue' in tags:
            for looking_for in self.LOOKING_FOR:
                if looking_for in tags:
                    self.looking_for = looking_for
                    return self.go_to_state('personal_issue')
        else:
            return self.finish('confused')


    # "finish" functions

    def finish_confused(self):
        """Send a message and go to the default state."""
        return "I think this problem might be out of my scope, or maybe I am not understanding properly." \
               "I can get you in touch with REHS if youd like: resed@oxy.edu!"


if __name__ == '__main__':
    OxyCSBot().chat()
