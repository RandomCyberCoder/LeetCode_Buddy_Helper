import pandas as pd
import sys
import random
import math
import datetime

def weight_function(days_since_last_solved):
    MAX_VALUE = 7
    GROWTH_RATE = 0.2
    MIDPOINT = 20

    #s-curve
    return MAX_VALUE / (1 + math.exp(GROWTH_RATE * (-days_since_last_solved + MIDPOINT)))

def choose_problem(problems, weights):
    if not problems:
        print("No problems found for the specified difficulty level.")
        return None
    
    return random.choices(range(len(problems)), weights=weights, k=1)[0]


def main():
    df = pd.read_csv('../data/problems.csv')
    names = set()
    urls = set()
    problems = []
    weights = []
    difficulty = sys.argv
    difficulty = difficulty[1] if len(difficulty) > 1 else None
    difficulty = difficulty.lower() if difficulty else None
    if difficulty not in ['easy', 'medium', 'hard', None]:
        print("Invalid difficulty level. Please choose from 'easy', 'medium', 'hard', or leave it blank for all.")
        return
    
    for index, row in df.iterrows():
        #skip duplicates
        if row["name"] in names or row["url"] in urls:
            print(f"Duplicate name: {row['name']} or Duplicate url: {row['url']}")
            continue
        #if difficulty is specified, skip rows that don't match the difficulty
        if difficulty and row['difficulty'].lower() != difficulty:
            continue
        problems.append({
            'name': row['name'],
            'difficulty': row['difficulty'],
            'url': row['url'],
            'idx': index
        })
        days_delta = datetime.datetime.now() - datetime.datetime.strptime(row['date_solved'], '%Y-%m-%d')
        #get days and make sure it's not negative
        days_delta = max(days_delta.days, 0)
        weights.append(weight_function(days_delta))

    choice = problems[choose_problem(problems, weights)]
    #update the date_solved to today for the chosen problem
    df.at[choice["idx"], 'date_solved'] = datetime.datetime.now().strftime('%Y-%m-%d')
    df.to_csv('../data/problems.csv', index=False)
    print(choice)
    
        
if __name__ == "__main__":
    main()