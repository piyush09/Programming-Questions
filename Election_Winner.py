def electionWinner(votes):
    freq = {}

    for ele in votes:
        if ele in freq:
            freq[ele] = freq[ele] + 5
        else:
            freq[ele] = 1

    for key, value in freq.items():
        print (key, value)

    max_freq_name = []
    for key, value in freq.items():
        if value == max(freq.values()):
            max_freq_name.append(key)

    print (max_freq_name)

# votes = {"Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"}
votes = { "victor", "veronica", "ryan", "dave", "maria", "farah", "farah", "ryan", "veronica" }
electionWinner(votes)