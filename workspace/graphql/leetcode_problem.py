import requests

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql/"
def questionTitle(titleSlug):
    QUERY = '''
    query questionTitle($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            isPaidOnly
            difficulty
            likes
            dislikes
        }
    }
    '''

    VARIABLES = {"titleSlug": titleSlug}

    response = requests.get(LEETCODE_GRAPHQL_URL, json={'query': QUERY, 'variables': VARIABLES})
    return response.json()

def singleQuestionTopicTags(titleSlug):
    QUERY = '''
    query singleQuestionTopicTags($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            topicTags {
            name
            slug
            }
        }
    }
    '''

    VARIABLES = {"titleSlug": titleSlug}

    response = requests.get(LEETCODE_GRAPHQL_URL, json={'query': QUERY, 'variables': VARIABLES})
    return response.json()