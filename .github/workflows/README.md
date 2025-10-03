# GitHub Actions Workflows

This directory contains automated workflows for the LangLawyer repository.

## Update Changelog Workflow

**File:** `update-changelog.yml`

### Purpose
Automatically updates the Changelog section in README.md whenever changes are pushed to the main or master branch.

### How It Works

1. **Trigger**: Runs on every push to `main` or `master` branches
2. **Extract Information**: 
   - Gets the commit message, author, and date
   - Identifies files changed in the commit
3. **Generate Entry**:
   - Creates a structured changelog entry with the commit message and author
   - Includes modified files (if reasonable number of files)
4. **Update README**:
   - Inserts the new entry at the top of the Changelog section
   - Preserves all existing changelog entries
5. **Commit & Push**:
   - Commits the updated README back to the repository
   - Uses `[skip ci]` flag to prevent infinite loops

### Safeguards

- **Infinite Loop Prevention**: Skips commits that contain "Update changelog" or "update-changelog" in the message
- **Skip CI Flag**: Uses `[skip ci]` in the commit message to prevent re-triggering the workflow
- **Change Detection**: Only commits if the README was actually modified

### Permissions

The workflow requires:
- `contents: write` - To commit and push changes
- `pull-requests: write` - For potential future PR integration

### Customization

To modify the changelog format, edit the `Generate changelog entry with AI` step in the workflow file.

### Troubleshooting

**Issue**: Workflow not running
- Check that the push is to `main` or `master` branch
- Verify GitHub Actions is enabled for the repository

**Issue**: Changes not being committed
- Check workflow logs in the Actions tab
- Verify that the bot has write permissions

**Issue**: Infinite loop detected
- The workflow has built-in protection against this
- If it occurs, check that the skip logic is working correctly

### Manual Testing

You can test the workflow locally using the following script:

```bash
# Simulate the changelog update
COMMIT_DATE=$(date +%Y-%m-%d)
CHANGELOG_ENTRY="- **Test commit** (Test Author)"

temp_file=$(mktemp)
awk -v date="$COMMIT_DATE" -v entry="$CHANGELOG_ENTRY" '
/^## Changelog/ {
  print
  print ""
  print "### " date
  print entry
  in_changelog=1
  next
}
in_changelog && /^### / {
  in_changelog=0
}
!in_changelog || /^### / {
  print
}
' README.md > "$temp_file"

diff README.md "$temp_file"
rm "$temp_file"
```
