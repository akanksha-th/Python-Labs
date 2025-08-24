import random

corpus =['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear', 'melon', 'car', 'bike', 'train', 
         'plane', 'boat', 'ship', 'house', 'building', 'apartment', 'mansion', 'cabin', 'tent', 
         'dog', 'cat', 'bird', 'fish', 'rabbit', 'horse', 'lion', 'elephant', 'zebra', 'giraffe', 
         'monkey', 'snake', 'spider', 'ant', 'bee', 'butterfly', 'dragonfly', 'grasshopper', 'mosquito',
           'whale', 'shark', 'dolphin', 'octopus', 'jellyfish', 'starfish', 'shell', 'coral', 'tree', 
           'flower', 'grass', 'bush', 'rock', 'mountain', 'hill', 'valley', 'river', 'lake', 'ocean', 
           'desert', 'forest', 'jungle', 'cave', 'waterfall', 'volcano', 'sky', 'cloud', 'rain', 'snow', 
           'storm', 'sun', 'moon', 'star', 'planet', 'galaxy', 'universe', 'earth', 'mars', 'venus', 
           'jupiter', 'saturn', 'neptune', 'uranus', 'mercury', 'pluto', 'astronaut', 'rocket', 'spaceship', 
           'alien', 'robot', 'computer', 'internet', 'software', 'hardware', 'code', 'language', 'keyboard', 
           'mouse', 'monitor', 'printer', 'scanner', 'camera', 'phone', 'tablet', 'laptop', 'desktop', 
           'server', 'database', 'file', 'folder', 'backup', 'download', 'upload', 'email', 'message', 
           'chat', 'social', 'media', 'network', 'website', 'blog', 'forum', 'search', 'engine', 'link', 
           'page', 'content', 'video', 'audio', 'image', 'document', 'spreadsheet', 'presentation', 'slide', 
           'text', 'font', 'style', 'format', 'color', 'theme', 'design', 'layout', 'interface', 'user', 
           'profile', 'account', 'login', 'password', 'security', 'privacy', 'policy', 'term', 'condition', 
           'agreement', 'contract', 'deal', 'offer', 'sale', 'discount', 'price', 'cost', 'value', 'quality', 
           'quantity', 'size', 'weight', 'length', 'width', 'height', 'depth', 'dimension', 'scale', 'measure',
             'unit', 'system', 'metric', 'imperial', 'standard', 'custom', 'service', 'support', 'help', 
             'assist', 'guide', 'instruction', 'manual', 'tutorial', 'lesson', 'class', 'school', 'college', 
             'university', 'academy', 'institution', 'education', 'learning', 'study', 'research', 'knowledge', 
             'information', 'data', 'fact', 'truth', 'theory', 'hypothesis', 'experiment', 'observation', 
             'analysis', 'interpretation', 'conclusion', 'result', 'outcome', 'report', 'document', 
             'publication', 'journal', 'paper', 'article', 'book', 'novel', 'story', 'poem', 'play', 'movie']

word = random.choice(corpus)

tries = 15
half_way = tries//1.5

def match_score(word, user_word):
    score = 0
    for ch1, ch2 in zip(word, user_word):
        if ch1==ch2:
            print(f"You got this right!!: {ch2}")
            score += 1
    return score

print('WELCOME TO WORD-MANIA!!')
while tries>0:
    user_word = input("Write your guess. ")
    if user_word==word:
        print("Yayy! You guessed it right!")
        tries = -1
    
    elif tries==half_way:
        print("Seems like you need a hint. ")
        first = word[0]
        last = word[-1]
        print(f"The first letter is {first} and the last letter is {last} and the word has {len(word)} letters. \n", '-'*50)
        tries -= 1
    else:
        tries -= 1
        score_value = match_score(word, user_word)
        match_percentage = score_value/len(word)
        print(f"NOPE!!! {tries} tries left.")
        match_percentage = round((score_value / len(word)) * 100,2)
        print(f'Your word matches {match_percentage} percentage with the word. \n', '-'*50)

if tries == 0:
    print("Sorry, you ran out of chances. The word was:", word)