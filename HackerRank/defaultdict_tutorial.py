from collections import defaultdict

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
n_words = [input() for _ in range(n)]
m_words = [input() for _ in range(m)]
n_dict = defaultdict(list)
for idx, word in enumerate(n_words):
    n_dict[word].append(idx+1)

for word in m_words:
    if word in n_dict:
        print(*n_dict[word])
    else:
        print(-1)
        
