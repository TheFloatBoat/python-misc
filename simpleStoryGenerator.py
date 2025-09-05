import random
berbs = ["will", "might", "can", "cannot", "will not", "might not", "shall", "shall not", "may"]
verbs = ["is" , "keeps" , "understands" , "has" , "lets" , "watches" , "does" , "begins" , "follows" , "says" , "seems" , "stops" , "goes" , "helps" , "creates" , "cans" , "talks" , "speaks" , "gets" , "turns" , "reads" , "would" , "starts" , "allows" , "makes" , "deletes" , "adds" , "knows" , "shows" , "spends" , "punches" , "hears" , "grows" , "thinks" , "plays" , "opens" , "takes" , "runs" , "walks" , "sees" , "moves" , "wins" , "comes" , "likes" , "offers" , "could" , "lives" , "remembers" , "wants" , "believes" , "loves" , "looks" , "holds" , "considers" , "uses" , "brings" , "appears" , "finds" , "happens" , "buys" , "gives" , "must" , "waits" , "tells" , "writes" , "serves" , "works" , "provides" , "dies" , "may" , "sits" , "sends" , "should" , "stands" , "expects" , "calls" , "loses" , "builds" , "tries" , "pays" , "stays" , "asks" , "meets" , "falls" , "needs" , "includes" , "cuts" , "feels" , "continues" , "reaches" , "becomes" , "sets" , "kills" , "leaves" , "learns" , "remains" , "puts" , "changes", "obliterates","consumes"]
nouns = ["gold", "painting", "grass", "parrot", "greece", "pencil", "guitar", "piano", "hair", "pillow", "hamburger", "pizza", "helicopter", "planet", "helmet", "plastic", "holiday", "portugese", "honey", "potato", "balloon", "horse", "queen", "banana", "hospital", "quill", "battery", "house", "rain", "beach", "hydrogen", "rainbow", "beard", "raincoat", "bed", "refrigerator", "Belgium", "restaurant", "boy", "iron", "river", "branch", "rocket", "breakfast", "jackal", "room", "brother", "jelly", "rose", "camera", "jewellery", "russia", "candle", "jordan", "sandwich", "car", "juice", "school", "caravan", "kangaroo", "scooter", "carpet", "king", "shampoo", "cartoon", "kitchen", "shoe", "china", "kite", "soccer", "church", "knife", "spoon", "crayon", "lamp", "stone", "crowd", "lawyer", "sugar", "daughter", "leather", "sweden", "death", "library", "teacher", "denmark", "lighter", "telephone", "diamond", "lion", "television", "dinner", "lizard", "tent", "disease", "lock", "Thai", "doctor", "london", "tomato", "dog", "lunch", "toothbrush", "dream", "machine", "traffic", "dress", "magazine", "train",  "magician", "truck", "manchester", "uganda", "market", "match", "van", "energy", "monkey", "microphone",  "nail", "whale", "vase", "vegetable", "morning", "vulture", "england", "motorcycle", "wall", "napkin", "window", "family", "needle", "wire", "finland", "nest", "xylophone", "fish", "nigeria", "yacht", "flag", "night", "yak", "flower", "notebook", "zebra", "football",  "zoo", "forest", "garden", "fountain", "orange", "gas", "france" , "girl", "furniture", "glass", "garage", "ghost" ]
nounv = ["actor","advertisement", "afternoon", "airport", "ambulance", "animal", "answer", "apple", "army", "Australian", "iceberg", "insect", "insurance", "island", "easter","egg", "eggplant", "umbrella", "egyptian", "oxygen", "oyster","elephant","engine", "evening", "eye","ocean", "oil"] 
adnoun = ["major" , "natural" , "new" , "better" , "significant" , "good" , "similar" , "high" , "strong" , "hot" , "possible" , "dead" , "great" , "whole" , "central" , "big" , "free" , "happy" , "military" , "serious" , "small" , "true" , "ready" , "large" , "federal" , "simple" , "national" , "left" , "young" , "full" , "physical" , "different" , "special" , "general" , "black" , "long" , "clear" , "financial" , "little" , "recent" , "blue" , "certain" , "democratic" , "political" , "personal" , "dark" , "bad" ,"various" , "white" , "red" , "real" , "difficult" , "close" , "best" , "legal" , "right" , "likely" , "religious" , "social" , "short" , "cold" , "single" , "final" , "public" , "medical" , "main" , "sure" , "current" , "green" , "low" , "wrong" , "nice" , "private" , "huge" , "past" , "popular" , "human" , "foreign" , "traditional" , "local" , "fine" , "cultural" , "late" , "common" , "hard" , "poor"]
adnounv = [ "open" , "entire" , "available" , "only" , "early" ,  "able" , "important" , "international" , "other" , "economic" , "old" , "easy" , "environmental" , "american"]
adverb = ["boldly" , "bravely" , "brightly" , "cheerfully" , "deftly" , "devotedly" , "eagerly" , "elegantly" , "faithfully" , "fortunately" , "gleefully" , "gracefully" , "happily" , "honestly" , "innocently" , "kindly" , "merrily" , "obediently" , "perfectly" , "politely" , "powerfully" , "safely" , "victoriously" , "warmly" , "vivaciously" , "achingly" , "angrily" , "annoyingly" , "anxiously" , "badly" , "boastfully" , "dejectedly" , "enviously" , "foolishly" , "hopelessly" , "irritably" , "jealously" , "joylessly" , "lazily" , "miserably" , "morosely" , "obnoxiously" , "painfully" , "poorly" , "rudely" , "sadly" , "selfishly" , "terribly" , "unhappily" , "wearily" , "always" , "daily" , "eventually" , "finally" , "frequently" , "generally" , "hourly" , "later" , "never" , "nightly" , "normally" , "occasionally" , "often" , "rarely" , "regularly" , "seldom" , "sometimes" , "soon" , "still" , "today" , "tomorrow" , "usually" , "weekly" , "yearly" , "yesterday" , "briskly" , "casually" , "expeditiously" , "fleetingly" , "gradually" , "haltingly" , "hastily" , "hurriedly" , "immediately" , "instantly" , "languidly" , "lazily" , "leisurely" , "promptly" , "quickly" , "rapidly" , "slowly" , "speedily" , "swiftly" , "tediously" , "audibly" , "deafeningly" , "ear-splittingly" , "emphatically" , "faintly" , "inaudibly" , "loudly" , "noiselessly" , "noisily" , "quietly" , "resonantly" , "resoundingly" , "shrilly" , "silently" , "softly" , "soundlessly" , "thunderously" , "uproariously" , "vociferously" , "weakly" , "accidentally" , "awkwardly" , "blindly" , "coyly" , "crazily" , "cruelly" , "defiantly" , "deliberately" , "doubtfully" , "dramatically" , "dutifully" , "enormously" , "excitedly" , "hungrily" , "madly" , "mortally" , "mysteriously" , "nervously" , "seriously" , "shakily" , "restlessly" , "solemnly" , "sternly" , "unexpectedly" , "wildly" ]
con = ["and", "if", "because", "or", "as", "while", "for"]
pun = [".", "!", "?", ";", ":"]
names = ["James" , "Mary" , "Robert" , "Patricia" , "John" , "Jennifer" , "Michael" , "Linda" , "David" , "Elizabeth" , "William" , "Barbara" , "Richard" , "Susan" , "Joseph" , "Jessica" , "Thomas" , "Sarah" , "Charles" , "Karen" , "Christopher" , "Lisa" , "Daniel" , "Nancy" , "Matthew" , "Betty" , "Anthony" , "Margaret" , "Mark" , "Sandra" , "Donald" , "Ashley" , "Steven" , "Kimberly" , "Paul" , "Emily" , "Andrew" , "Donna" , "Joshua" , "Michelle" , "Kenneth" , "Carol" , "Kevin" , "Amanda" , "Brian" , "Dorothy" , "George" , "Melissa" , "Timothy" , "Deborah" , "Ronald" , "Stephanie" , "Edward" , "Rebecca" , "Jason" , "Sharon" , "Jeffrey" , "Laura" , "Ryan" , "Cynthia" , "Jacob" , "Kathleen" , "Gary" , "Amy" , "Nicholas" , "Angela" , "Eric" , "Shirley" , "Jonathan" , "Anna" , "Stephen" , "Brenda" , "Larry" , "Pamela" , "Justin" , "Emma" , "Scott" , "Nicole" , "Brandon" , "Helen" , "Benjamin" , "Samantha" , "Samuel" , "Katherine" , "Gregory" , "Christine" , "Alexander" , "Debra" , "Frank" , "Rachel" , "Patrick" , "Carolyn" , "Raymond" , "Janet" , "Jack" , "Catherine" , "Dennis" , "Maria" , "Jerry" , "Heather" , "Tyler" , "Diane" , "Aaron" , "Ruth" , "Jose" , "Julie" , "Adam" , "Olivia" , "Nathan" , "Joyce" , "Henry" , "Virginia" , "Douglas" , "Victoria" , "Zachary" , "Kelly" , "Peter" , "Lauren" , "Kyle" , "Christina" , "Ethan" , "Joan" , "Walter" , "Evelyn" , "Noah" , "Judith" , "Jeremy" , "Megan" , "Christian" , "Andrea" , "Keith" , "Cheryl" , "Roger" , "Hannah" , "Terry" , "Jacqueline" , "Gerald" , "Martha" , "Harold" , "Gloria" , "Sean" , "Teresa" , "Austin" , "Ann" , "Carl" , "Sara" , "Arthur" , "Madison" , "Lawrence" , "Frances" , "Dylan" , "Kathryn" , "Jesse" , "Janice" , "Jordan" , "Jean" , "Bryan" , "Abigail" , "Billy" , "Alice" , "Joe" , "Julia" , "Bruce" , "Judy" , "Gabriel" , "Sophia" , "Logan" , "Grace" , "Albert" , "Denise" , "Willie" , "Amber" , "Alan" , "Doris" , "Juan" , "Marilyn" , "Wayne" , "Danielle" , "Elijah" , "Beverly" , "Randy" , "Isabella" , "Roy" , "Theresa" , "Vincent" , "Diana" , "Ralph" , "Natalie" , "Eugene" , "Brittany" , "Russell" , "Charlotte" , "Bobby" , "Marie" , "Mason" , "Kayla" , "Philip" , "Alexis" , "Louis" , "Lori"]
shortlist = ["he", "she"]
blips = ["a","the"]

def randomword(a):
    return a[random.randint(0,len(a)-1)]


def senfrag():
    c=""
    if random.randint(1,3) == 1:
        if random.randint(1,5) == 1:
            c = c + "the "
        c = c + randomword(adnoun) + " "
        
    c = c + randomword(shortlist)

    if random.randint(0,1) == 1:
        c = c + " " + randomword(berbs)
    if random.randint(0,1) == 1:
        c = c + " " + randomword(adverb)

    c = c + " "+ randomword(verbs)

    if random.randint(1,2) == 1:
        if random.randint(1,2) == 1:
            c = c +" " + randomword(blips)
        if random.randint(0,1) == 1:
           c = c + " " + randomword(adnoun)
        c = c + " " + randomword(nouns)
    else:
        if random.randint(1,2) == 1:
            c = c +" an"
        if random.randint(0,1) == 1:
            c = c + " " + randomword(adnounv)
            if random.randint(0,1) == 1:
                c = c + " " + randomword(nounv)
            else:
                c = c + " " + randomword(nouns)
        else:
            c = c + " " + randomword(nounv)
    return c

def sentence():
    a = random.randint(1,3)
    b = ""
    if a == 1:
        b = senfrag()+ randomword(pun)
    elif a == 2:
        b = senfrag()+ " " + randomword(con) + " " + senfrag() +randomword(pun)
    else:
        b = randomword(con) + " " + senfrag() + ", " + senfrag() + randomword(pun) 

    b = b[0].upper() + b[1:]

    return b

def para():
    b = random.randint(1,25)
    c = "   " + sentence()
    for x in range(1, b):
        c=c+" "+sentence()
    return c

def chapter(a):
    b = random.randint(1,25)
    c = "Chapter " + str(a) + "\n" + para()
    for x in range(1, b):
        c=c+ "\n\n" +para()
    return str(c)

def title():
    return randomword(blips).capitalize() + " " + randomword(adnoun) + " " + randomword(nouns)

def story():
    b = random.randint(1,25)
    c = title()
    for x in range(1, b):
        c=c+ "\n \n"+chapter(x)
    c =c + "\n\n\n\n\nThe End."
    return c
  
for n in range(1,5):
    a = random.randint(0, len(names)-1)
    shortlist.append(names[a])
with open('story.txt', 'w') as f:
  f.write(story())
