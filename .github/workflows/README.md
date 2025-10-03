# GitHub Actions Workflows

This directory contains automated workflows for the LangLawyer repository.

## Update Changelog Workflow

**File:** `update-changelog.yml`

### Purpose
Automatically updates the Changelog section in README.md whenever changes are pushed to the main or master branch using GitHub Copilot AI-powered changelog generation.

### How It Works

1. **Trigger**: Runs on every push to `main` or `master` branches
2. **Extract Information**: 
   - Gets the commit message, author, and date
   - Identifies files changed in the commit
   - Extracts commit body and diff statistics
3. **Generate Entry with GitHub Copilot**:
   - **AI-Powered Generation**: Uses GitHub Copilot to generate a user-friendly changelog entry
   - GitHub Copilot analyzes the commit message, changed files, and diff statistics
   - Generates concise, meaningful descriptions focused on what changed and why
   - **Fallback**: If AI is unavailable or fails, uses template-based generation
4. **Update README**:
   - Inserts the new entry at the top of the Changelog section
   - Preserves all existing changelog entries
5. **Commit & Push**:
   - Commits the updated README back to the repository
   - Uses `[skip ci]` flag to prevent infinite loops

### AI Integration

The workflow uses GitHub Copilot (via GitHub Models API) to generate meaningful changelog entries. GitHub Copilot:
- Analyzes commit messages, file changes, and code diffs
- Generates user-facing descriptions (not implementation details)
- Creates structured, concise entries with 2-4 bullet points
- Focuses on the impact of changes for users and developers

**Configuration**: The workflow uses the built-in `GITHUB_TOKEN` for authentication, so no additional API keys are required. GitHub Copilot generation is automatically enabled.

### Files

- `update-changelog.yml` - Main workflow file
- `generate_changelog_ai.py` - Python script that calls GitHub Copilot API

### Safeguards

- **Infinite Loop Prevention**: Skips commits that contain "Update changelog" or "update-changelog" in the message
- **Skip CI Flag**: Uses `[skip ci]` in the commit message to prevent re-triggering the workflow
- **Change Detection**: Only commits if the README was actually modified
- **Error Handling**: Falls back to template generation if AI call fails

### Permissions

The workflow requires:
- `contents: write` - To commit and push changes
- `pull-requests: write` - For potential future PR integration

### Customization

To modify the AI prompt or changelog format:
1. Edit `generate_changelog_ai.py` to change the prompt template
2. Edit the fallback logic in the workflow file for non-AI generation

### Troubleshooting

**Issue**: Workflow not running
- Check that the push is to `main` or `master` branch
- Verify GitHub Actions is enabled for the repository

**Issue**: GitHub Copilot generation fails
- Check workflow logs for API error messages
- Verify the repository has access to GitHub Models API
- The workflow will fall back to template-based generation

**Issue**: Changes not being committed
- Check workflow logs in the Actions tab
- Verify that the bot has write permissions

**Issue**: Infinite loop detected
- The workflow has built-in protection against this
- If it occurs, check that the skip logic is working correctly

### Example Output

With GitHub Copilot enabled:
```markdown
### 2025-01-04
- **Implement user authentication system** (Jane Developer)
  - Added JWT-based authentication for secure API access
  - Implemented user registration and login endpoints
  - Enhanced security with password hashing and validation
```

Without AI (fallback):
```markdown
### 2025-01-04
- **Implement user authentication system** (Jane Developer)
  - Modified: src/auth/jwt.py, src/api/auth_routes.py, tests/test_auth.py
```
