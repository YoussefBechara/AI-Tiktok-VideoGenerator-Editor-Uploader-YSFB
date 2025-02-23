import praw
import regex as re
from setup import get_credential

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def gather_reddit_facts(num_of_facts, num_of_facts_to_skip, timeout=60):
    # Initialize Reddit API credentials
    reddit = praw.Reddit(
        client_id=get_credential("reddit_client_id"),
        client_secret=get_credential("reddit_client_secret"),
        user_agent=get_credential("reddit_user_agent")
    )

    # Fetch stories from r/stories
    subreddit = reddit.subreddit('facts')
    facts_list = []

    # Adjusted the timeout handling
    for i, submission in enumerate(subreddit.top(time_filter ='all')):
        # Skip the facts that the user wants to skip
        if i < num_of_facts_to_skip:
            continue

        try:
            content = submission.selftext
        except praw.exceptions.RequestException as e:
            print(f"Error fetching content for submission {submission.id}: {e}")
            continue  # Skip this submission and move on to the next one

        content_without_emojis = remove_emojis(content)
        facts_list.append({
            'title': submission.title,
            'content': content_without_emojis,
        })

        # Stop fetching when we have enough facts
        if len(facts_list) >= num_of_facts:
            break

    return facts_list  # Return the entire list of facts, each with a title and content

if __name__ == '__main__':
    facts = gather_reddit_facts(1, 1)
    for fact in facts:
        print(f"Fact: {fact['title']}\nSource: {fact['content']}\n")
