import typer
import json
import requests
from typing_extensions import Annotated


def main(
    username: Annotated[str, typer.Argument(help="The user name to get activity from")]
):
    headers = {'Accept': 'application/vnd.github+json'}
    end_point = f"https://api.github.com/users/{username}/events"

    
    response = requests.get(end_point, headers=headers)

    if response.status_code == 404:
        print('User not found')
    else:
        events = response.json()
        if not events:
            print('No recent activity found for this user')
        else:
            for event in events:
                repo_name = event.get('repo',{}).get('name','No repo')
                event_type = event.get('type', 'No type')
                created_at = event.get('created_at','No date')

                print(f"\nRepository: {repo_name}")
                print(f"Event Type: {event_type}")
                print(f"Date: {created_at}")

if __name__ == "__main__":
    typer.run(main)
    