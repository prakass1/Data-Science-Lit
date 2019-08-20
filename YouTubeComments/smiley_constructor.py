class Smileys:
    '''
        Converts smileys into word format. Note: There are some new formats like hugging face which is not handled here.
        Needs a separate initialization for it.
        Rabin Karps will be implemented soon
    '''


    def __init__(self, emotion):
        self.emotions = emotion
        pass

    def detect_word4smiley(self, text):
        def compute(word):
            if word in self.emotions.keys():
                return self.emotions[word]

            #Super Search Here
            else:
                #Super Random Search Strategy
                '''
                Steps:
                1. Pick a random key from smiley keys. 
                2. Perform a pattern search
                    Idea:
                    Implement a forward search strategy 
                    on the pairs using a pattern search algorithm such as rabin karp
                '''
                return word
        return " ".join(compute(word) for word in text.split())


emotions = {
        "(.V.)": "Alien",
        "(.v.)": "Alien",
        "o:-)": "Angel",
        "O:-)": "Angel",
        "X-(": "Angry",
        "x-(": "Angry",
        "~:0": "Baby",
        ":-D": "Big Grin",":-d": "Big Grin",
        "(*v*)": "Bird",
        ":-#": "Braces",
        "</3": "Broken Heart",
        "=^.^=": "Cat",
        "*<:o)": "Clown",
        "O.o": "Confused",
        "B-)": "Cool","b-)": "Cool",
        ":_(": "Crying",
        ":'(": "Crying",
        "\:D/": "Dancing","\:d/": "Dancing",
        "*-*": "Dazed",
        ":o3": "Dog",
        "#-o": "Doh!",
        ":*)": "Drunk",
        "//_^": "Emo",
        ">:)": "Evil Grin",
        "<><": "Fish",
        ":-(": "Frown",
        ":(	": "Frown",
        ":-(": "Frowning",
        "=P": "Frustrated","=p": "Frustrated",
        ":-P": "Frustrated",":-p": "Frustrated",
        "8-)": "Glasses",
        "$_$": "Greedy",
        ":->": "Grin",
        "=)": "Happy",
        ":-)": "Happy",
        ":)": "Happy",
        "#": "Hashtag",
        "<3": "Heart",
        "{}": "Hug",
        ":-|": "Indifferent",
        "X-p": "Joking",
        ":-)*": "Kiss",
        ":-*": "Kiss",
        ":*": "Kiss",
        "(-}{-)": "Kissing",
        "XD": "Laughing","xd": "Laughing",":xd": "Laughing",
        "=D": "Laughing Out Loud","=d": "Laughing Out Loud",
        ")-:": "Left-handed Sad Face",
        "(-:": "Left-handed Smiley Face",
        "<3": "Love",
        "=/": "Mad",
        ":-)(-:": "Married",
        "@": "Mention",
        "<:3)~": "Mouse",
        "~,~": "Napping",
        ":-B": "Nerd",":-b": "Nerd",
        "^_^": "Overjoyed",
        "<l:0": "Partying",
        ":-/": "Perplexed",
        "=8)": "Pig",
        "=(": "Sad",
        ":-(": "Sad",
        ":(": "Sad",
        ":S": "Sarcastic",":s": "Sarcastic",
        ":-@": "Screaming",
        "=O": "Shocked",
        ":-o": "Shocked",
        ":-)": "Smile",
        ":)": "Smile",
        ":-Q": "Smoking",":-q": "Smoking",
        ":>": "Smug",
        ":P": "Sticking Tongue Out",":p": "Sticking Tongue Out",
        ":o": "Surprised",":O": "Surprised",
        ":-J": "Tongue in Cheek",":-j": "Tongue in Cheek",
        ":-&": "Tongue Tied",
        "=-O": "Uh-oh","=-o": "Uh-oh",
        ':-\\': "Undecided",
        ":-E": "Vampire",":-e": "Vampire",
        "=D": "Very Happy","=d": "Very Happy",":D": "Very Happy",":d": "Very Happy",
        ";-)": "Winking",
        ";)": "Winking",
        "|-O": "Yawn",
        "8-#": "Zombie"
}

def main():
    sm = Smileys(emotions)
    # Smileys should be by space else will not work currently
    print(sm.detect_word4smiley("weqwsdea. :) ..."))

#main()
