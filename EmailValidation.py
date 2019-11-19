def getEmail():
    email = input("Please enter your email address: ")
    return email

def validDomain(str):
    valid = False
    count = 0
    i = 0
    top_domains = [".mil", ".org", ".net", ".int", ".edu", ".gov", ".com", ".arpa", ".ac", \
                    ".ad", ".ae", ".af", ".ag", ".ai", ".al", ".am", ".an", ".ao", ".aq", \
                    ".ar", ".as", ".at", ".au", ".aw", ".ax", ".az", ".ba", ".bb", ".bd", \
                     ".be", ".bf", ".bg", ".bh", ".bi", ".bj", ".bl", ".bm", ".bn", ".bo", \
                    ".bq", ".br", ".bs", ".bt", ".bv", ".bw", ".by", ".bz", ".ca", ".cc" \
                    ".cd", ".cf", ".cg", ".ch", ".ci", ".ck", ".cl", ".cm", ".cn", ".co", \
                    ".cr", ".cu", ".cv", ".cw", ".cx", ".cy", ".cz", ".dd", ".de", ".dj", \
                    ".dl", ".dm", ".do", ".dz", ".ec", ".ee", ".eg", ".eh", ".er", ".es", \
                    ".et", ".eu", ".fi", ".fj", ".fk", ".fm", ".fo", ".fr", ".ga", ".gb", \
                    ".gd", ".ge", ".gf", ".gg", ".gh", ".gi", ".gl", ".gm", ".gn", ".gp", \
                    ".gq", ".gr", ".gs", ".gt", ".gu", ".gw", ".gy", ".hk", ".hm", ".hn", \
                    ".hr", ".ht", ".hu", ".id", ".ie", ".il", ".im", ".in", ".io", ".iq", \
                    ".ir", ".is", ".it", ".je", ".jm", ".jo", ".jp", ".ke", ".kg", ".kh", \
                    ".ki", ".km", ".kn", ".kp", ".kr", ".kw", ".ky", ".kz", ".la", ".lb", \
                    ".lc", ".li", ".lk", ".lr", ".ls", ".lt", ".lu", ".lv", ".ly", ".ma", \
                    ".mc", ".md", ".me", ".mf", ".mg", ".mh", ".mk", ".ml", ".mm", ".mn", \
                    ".mo", ".mp", ".mq", ".mr", ".ms", ".mt", ".mu", ".mv", ".mw", ".mx", \
                    ".my", ".mz", ".na", ".nc", ".ne", ".nf", ".ng", ".ni", ".nl", ".no", \
                    ".np", ".nr", ".nu", ".nz", ".om", ".pa", ".pe", ".pf", ".pg", ".ph", \
                    ".pk", ".pl", ".pm", ".pn", ".pr", ".ps", ".pt", ".pw", ".py", ".qa", \
                    ".re", ".ro", ".rs", ".ru", ".rw", ".sa", ".sb", ".sc", ".sd", ".se", \
                    ".sg", ".sh", ".si", ".sj", ".sk", ".sl", ".sm", ".sn", ".so", ".sr", \
                    ".ss", ".st", ".su", ".sv", ".sx", ".sy", ".sz", ".tc", ".td", ".tf", \
                    ".tg", ".th", ".tj", ".tl", ".tk", ".tm", ".tn", ".to", ".tp", ".tr", \
                    ".tt", ".tv", ".tw", ".tz", ".ua", ".eg", ".uk", ".us", ".uy", ".uz", \
                    ".va", ".vc", ".ve", ".vg", ".vi", ".vn", ".vu", ".wf", ".ws", ".xk", \
                    ".ye", ".yt", ".za", ".zm", ".zr", ".zw"]
    for i in range(len(top_domains)):
        if top_domains[i] in str:
            valid  = True
            count = count + 1
    if ".com" in str:
        count = 1
   
    
    if count > 1:
        valid = False
    return valid



def validateEmail(str):
    valid_email = True
    char_count = 0
    at_symbol = 0
    i = 0

    if "@" not in str:
        print(str + " is not a valid email address")
        return False
        
    while str[i] != '@':
        prev_count = char_count
        if str[0] == '.':
            valid_email = False
        elif str[i] == '.':
            char_count = char_count + 1
        for a in range(26):
            if str[i] == chr(a + 65):
                char_count = char_count + 1
            elif str[i] == chr(a + 97):
                char_count = char_count + 1
        for b in range(10):
            if str[i] == chr(b + 48):
                char_count = char_count + 1
        if char_count == prev_count:
            valid_email = False
        i = i + 1
      
        
    if char_count < 3:
        valid_email = False
    if str[i] == '@':
        i = i + 1

    while i != len(str):
        if str[i] == '@':
            valid_email = False
        elif str[i] == '.':
            char_count = char_count + 1
        for a in range(26):
            if str[i] == chr(a + 65):
                char_count = char_count + 1
            elif str[i] == chr(a + 97):
                char_count = char_count + 1
        for b in range(10):
            if str[i] == chr(b + 48):
                char_count = char_count + 1
        if char_count == prev_count:
            valid_email = False
        i = i + 1

    if validDomain(str[prev_count:len(str)]) == False:
        print(str + " is not a valid email address")
        
    elif valid_email == True:
        print(str + " is a valid email address")

    elif valid_email == False:
        print(str + " is not a valid email address")
    
def main():
        validateEmail(getEmail())
    

     
main()                 
                 
        
