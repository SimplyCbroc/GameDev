#load program
def load():
    save = open('save.txt', 'r')
    if save.read() == '':
        save.close()
        return('empty')
    else:
        save.close()
        return save.read()

def save(text):
    save = open('save.txt', 'w')
    save.write(text)
    save.close()
    
    
    
        
    
