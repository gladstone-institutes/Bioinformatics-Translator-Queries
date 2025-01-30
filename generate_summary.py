from github import Github
from collections import Counter
import datetime
import os

# GitHub token from environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY")  # Automatically populated by GitHub Actions

# Connect to GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Fetch issues
issues = repo.get_issues(state="all")

# Initialize data structures
open_count = 0
label_counts = Counter()
monthly_counts = Counter()

# Process issues
for issue in issues:
    if issue.state == "open":
        open_count += 1

    for label in issue.labels:
        label_counts[label.name] += 1

    if issue.created_at > datetime.datetime.now() - datetime.timedelta(days=365):
        month = issue.created_at.strftime("%Y-%m")
        monthly_counts[month] += 1

# Generate markdown content
markdown_content = f"# GitHub Issues Summary\n\n"
markdown_content += f"**Total Issues:** {issues.totalCount}\n"
markdown_content += f"**Open Issues:** {open_count}\n"
markdown_content += f"**Closed Issues:** {issues.totalCount - open_count}\n\n"

markdown_content += "## Labels\n"
for label, count in label_counts.items():
    markdown_content += f"- **{label}:** {count}\n"

markdown_content += "\n## Issues by Month (Last Year)\n"
for month, count in sorted(monthly_counts.items()):
    markdown_content += f"- **{month}:** {count}\n"

# Save to markdown file
output_file = "ISSUES_SUMMARY.md"
with open(output_file, "w") as f:
    f.write(markdown_content)

print(f"Markdown summary created as {output_file}.")
