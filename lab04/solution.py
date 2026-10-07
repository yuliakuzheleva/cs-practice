names =['Аня', 'Боря', 'Вика']
scores = [7.0, 9.0, 9.0]
def winner(names, scores):
    best = 0
    for i in range(1, len(scores)):
        if scores[i]>scores[best]:
            best = i
    return names[best]
if __name__== "__main__":
    names =['Аня', 'Боря', 'Вика']
    scores = [7.0, 9.0, 9.0]
    print(winner(names, scores))
def avarage(scores):
    if not scores:
        return 0.0
    return round(sum(scores)/len(scores), 2)
