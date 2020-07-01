import pandas as pd 

def main():
    # File paths
    big_file = "election_data.csv"
    small_file = "election_data_small.csv"

    # Open file
    df = pd.read_csv(big_file)

    # Calculate the total number of votes
    vote_count = df["Voter ID"].count()

    # List of candidates who received votes
    # Total number of votes each candidate won
    candidates = df["Candidate"].value_counts().keys().tolist()
    candidate_votes = df["Candidate"].value_counts().tolist()

    # Percentage of votes each candidate won
    vote_percents = list(map(lambda v : v/vote_count*100, candidate_votes))

    # Put all of the results together 
    zipped_list = list(zip(candidates, vote_percents, candidate_votes))

    # The winner of the election based on popular vote
    winner = candidates[candidate_votes.index(max(candidate_votes))]

    # Print analysis
    results = f'Election Results\n-------------------------\nTotal Votes: {vote_count}\n-------------------------\n'
    for data in zipped_list:
        results += f'{data[0]}: {data[1]:.3f}% ({data[2]})\n'
    results += f'-------------------------\nWinner: {winner}\n-------------------------'
    print(results)

    # Create text file with results
    results_file = open("py_poll_results.txt","w")
    results_file.write(results)
    results_file.close() 


main()
