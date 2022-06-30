def timeToMin(time):
    HH, MM = time.split(':')
    return int(HH) * 60 + int(MM)  

def solution(m, musicinfos):
        
    dic =  {'C#':'!', 'D#' : '@', 'F#': '^', 'G#' : '$', 'A#' : '%' }
    music = []
    
    for i in range(len(musicinfos)):
        
        start, end, name, song = musicinfos[i].split(',')
        music.append([i, timeToMin((start)), timeToMin((end)), name, song])
    
    music.sort(key=lambda x: ((x[1]-x[2]), x[0]))
    
    for k, v in dic.items():
        m = m.replace(k, v)
        
        for i in range(len(musicinfos)):
            music[i][4] = music[i][4].replace(k, v)
            
    for index, start, end, name, song in music:
        time = end - start
        
        word =  ''
        
        if len(song)>=time:
            word = song[:time]
        else:
            word = song * ((time) // len(song))
            word += song[:(time) % len(song)]
        
        if m in word:
            return name
    
    return '(None)'
