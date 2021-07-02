if __name__ == '__main__':
  scores = list()
  min_score = 0
  for _ in range(int(input())):
    name = input()
    score = float(input())
    if score < min_score:
      min_score = score
    scores.append([name,score])