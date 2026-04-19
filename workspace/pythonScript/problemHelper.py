import pandas as pd
import sys
import random


def choose_problem(problems):
    if not problems:
        print("No problems found for the specified difficulty level.")
        return None
    
    print(random.choices(problems, k=1)[0])


def main():
    df = pd.read_csv('../data/problems.csv')
    names = set()
    urls = set()
    problems = []
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
            'url': row['url']
        })

    choose_problem(problems)

        
if __name__ == "__main__":
    main()