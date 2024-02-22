import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
# Responses -------------------------------------------------------------------------------------------------------
    response('KRCT',['which','college','are','you','work','for'],required_words=('which','college'))
    response('I am a KRCTbot',['what','is','your','name'],required_words=['what','name'])
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(long.R_ADVICE, ['I', 'need','more','information'], required_words=['information','more','more'])
    response(long.R_EATING, ['what', 'is', 'your','purpose'],['waht','purpose','are','you','for','?'], required_words=['purpose'])
    response(long.R_RANK, ['what', 'is','the','ranking','of','your','college'], required_words=['ranking'])
    response(long.R_DEPT, ['what' ,'are ','the ','department' ,'avalable'], required_words=['department'])
    response(long.R_degree, ['what', 'degrees','are','avalable'], required_words=['degrees'])
    response(long.R_cutoff, ['cutoff', 'requirments'],['cuttoff','needed'], required_words=['cutoff'])        
    response(long.R_tution, ['tution','fee', 'details'],['fee','structure'], required_words=['tution'])
    response(long.R_hostal, ['hostal', 'fee','details'],['hostal','details'], required_words=['hostal'])
    response(long.R_cantien, ['cantien', 'facilites'],['cantien','details'], required_words=['cantien'])
    response(long.R_location, ['location', 'details'],['location','of','college'], required_words=['location'])
    response(long.R_placement, ['placement', 'details'], required_words=['placement'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
