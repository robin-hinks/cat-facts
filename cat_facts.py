import requests
import time

cat_facts = [
'More than half of the world\'s felines don\'t respond to catnip. Scientists still don\'t know quite why some kitties go crazy for the aromatic herb and others don\'t, but they have figured out that catnip sensitivity is hereditary. If a kitten has one catnip-sensitive parent, there\'s a one-in-two chance that it will also grow up to crave the plant. And if both parents react to catnip, the odds increase to at least three in four.', 
'According to a Hebrew legend, God created cats after Noah prayed for help in protecting the food stores on the Ark from being eaten by rats. In return, God made a lion sneeze and out came a pair of cats.',
'While it is commonly thought that the ancient Egyptians were the first to domesticate cats, the oldest known pet cat was recently found in a 9,500-year-old grave on the Mediterranean island of Cyprus. This grave predates early Egyptian art depicting cats by 4,000 years or more.',
'When cats bring you a dead bird or a mouse, it\'s not a sign of affection but instead to let you know you suck at hunting.',
'A cat\'s spine is so flexible because it\'s made up of 53 loosely fitting vertebrae. Humans only have 34. ',
'Thanks for participating in Cat Facts!'
] #7 texts

phone_numbers = ['5555555555'] #put phone numbers in this list


for i in range(len(cat_facts)):
    for j in range (len(phone_numbers)):
        resp = requests.post('https://textbelt.com/text', {
        'phone': phone_numbers[j],
        'message': cat_facts[i],
        'key': '2e523a8988810abdd8e4857139e8fdc10c4f8a49MWRE4R5DcGA8145LZQcBq7ThC',
        })
        print(resp.json())
    time.sleep(3600) #edit this to adjust time between messages
