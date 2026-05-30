async def process_github_issue_webhook(payload):

    return {
        "owner": payload.repository.owner.login,
        "repo": payload.repository.name,
        "issue_number": payload.issue.number,
        "title": payload.issue.title,
        "body": payload.issue.body
    }