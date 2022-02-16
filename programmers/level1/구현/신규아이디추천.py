def solution(new_id):
    
    myId = str(new_id)
    myId = myId.lower()
    myId = re.sub(r'[^a-z0-9-_.]','', myId)
    myId = re.sub('\.+', '.', myId)
    myId = re.sub('^[.]|[.]$', '', myId)
    if not myId:
        myId = 'a'
    if(len(myId)>=16):
        myId = myId[:15]
        while(myId and myId[-1]=='.'):
            myId = myId[:len(myId)-1]
    while(len(myId)<=2):
        myId = myId + myId[-1]
    return myId
