# GitHub Actions Workflows

This directory contains automated workflows for the LangLawyer repository.

## Update Changelog Workflow

**File:** `update-changelog.yml`

### Purpose
Automatically updates the Changelog section in README.md whenever changes are pushed to the main or master branch using AI-powered changelog generation.

### How It Works

1. **Trigger**: Runs on every push to `main` or `master` branches
2. **Extract Information**: 
   - Gets the commit message, author, and date
   - Identifies files changed in the commit
   - Extracts commit body and diff statistics
3. **Generate Entry with AI**:
   - **AI-Powered Generation**: Calls OpenAI API (GPT-3.5-turbo) to generate a user-friendly changelog entry
   - The AI analyzes the commit message, changed files, and diff statistics
   - Generates concise, meaningful descriptions focused on what changed and why
   - **Fallback**: If AI is unavailable or fails, uses template-based generation
4. **Update README**:
   - Inserts the new entry at the top of the Changelog section
   - Preserves all existing changelog entries
5. **Commit & Push**:
   - Commits the updated README back to the repository
   - Uses `[skip ci]` flag to prevent infinite loops

### AI Integration

The workflow uses OpenAI's GPT-3.5-turbo model to generate meaningful changelog entries. The AI:
- Analyzes commit messages, file changes, and code diffs
- Generates user-facing descriptions (not implementation details)
- Creates structured, concise entries with 2-4 bullet points
- Focuses on the impact of changes for users and developers

**Configuration**: Set the `OPENAI_API_KEY` secret in your repository settings to enable AI generation.
- Navigate to Settings → Secrets and variables → Actions → New repository secret
- Name: `OPENAI_API_KEY`
- Value: Your OpenAI API key

**Without API Key**: The workflow will use a fallback template-based generation that includes the commit message and list of modified files.

### Files

- `update-changelog.yml` - Main workflow file
- `generate_changelog_ai.py` - Python script that calls OpenAI API

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

**Issue**: AI generation fails
- Verify `OPENAI_API_KEY` secret is set correctly
- Check workflow logs for API error messages
- The workflow will fall back to template-based generation

**Issue**: Changes not being committed
- Check workflow logs in the Actions tab
- Verify that the bot has write permissions

**Issue**: Infinite loop detected
- The workflow has built-in protection against this
- If it occurs, check that the skip logic is working correctly

### Example Output

With AI enabled:
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
