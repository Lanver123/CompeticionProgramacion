import sys

if __name__ == '__main__':

    num_cases = int(input())
    while num_cases > 0:
        num_cases -= 1
        line = ''
        while len(line) == 0:
            line = input().strip()
        num_candidates = int(line)

        candidates = []
        for i in range(num_candidates):
            candidates.append(input().strip())
        
        ballots = []
        while True:
            try:
                line = None
                line = input()
            except:
                pass
            if line is None: break
            line = line.strip()
            if len(line) == 0: break
            ballot = [int(x) - 1 for x in line.split()]
            ballots.append(ballot)
        active_candidates = [True] * len(candidates)
        
        not_finished = True
        while not_finished:
            votes = [0] * len(candidates)
            #count votes
            for ballot in ballots:
                for voteCandidate in ballot:
                    if active_candidates[voteCandidate]:
                        votes[voteCandidate] += 1
                        break

            maxVotes = max(votes)
            minVotes = maxVotes
            for candidate in range(len(votes)):
                if active_candidates[candidate] and votes[candidate] < minVotes:
                    minVotes = votes[candidate]

            if maxVotes == minVotes:
                for candidate in range(len(votes)):
                    if active_candidates[candidate]:
                        print(candidates[candidate])
                        not_finished = False
            # winner
            elif (maxVotes * 2) > len(ballots):
                for candidate in range(len(votes)):
                    if votes[candidate] == maxVotes:
                        print(candidates[candidate])
                        not_finished = False
                        break
            else:
                for candidate in range(len(votes)):
                    if votes[candidate] == minVotes:
                        active_candidates[candidate] = False
        
        if num_cases > 0:
            print()