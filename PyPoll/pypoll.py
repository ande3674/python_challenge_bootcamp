import pandas as pd 

def main():
    # File paths
    file = "election_data.csv"
    small_file = "election_data_small.csv"

    # Open file
    small_df = pd.read_csv(small_file)

    # Calculate the total number of votes
    vote_count = small_df["Voter ID"].count()

    # List of candidates who received votes
    # Total number of votes each candidate won
    # candidate_counts = small_df["Candidate"].value_counts()
    # dict(candidate_counts)
    candidates = small_df["Candidate"].value_counts().keys().tolist()
    candidate_votes = small_df["Candidate"].value_counts().tolist()

    # Percentage of votes each candidate won
    vote_percents = list(map(lambda v : v/vote_count*100, candidate_votes))

    zipped_list = list(zip(candidates, vote_percents, candidate_votes))

    # The winner of the election based on popular vote
    winner = candidates[candidate_votes.index(max(candidate_votes))]

    # Print analysis
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {vote_count}')
    print('-------------------------')
    for data in zipped_list:
        print(f'{data[0]}: {data[1]:.3f}% ({data[2]})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

    # Create text file with results


main()