def main():
    import re
    wp = open('WhatsApp.html', 'r', encoding='utf-8')
    wps = wp.read()
    mensajes = re.findall(r"<span class=\"emojitext selectable-text\"[\s\S]*?><!-- react-text: [0-9]* -->([\s\S]+?[^<]*)", wps)
    puntuaciones, punt, promedios = [], [], []
    for i in mensajes:
        if i.isdigit():
            if int(i) <= 10 :
                punt.append(int(i))
        elif "*" in i:
            puntuaciones.append(punt)
            punt = []
    puntuaciones.append(punt)
    for p in puntuaciones:
        if len(p) > 0:
            a = round(sum(p)/float(len(p)), 2)
            promedios.append(a)
    return promedios
puntajes = main()
y = open('puntajes.txt', 'a+')
for p in puntajes:
    y.write(str(p) + '\n')
y.close()
