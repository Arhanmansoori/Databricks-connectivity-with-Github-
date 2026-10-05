# Databricks Free Edition + GitHub Version Control

A practical starter guide for connecting **Databricks Free Edition** to **GitHub** using **Databricks Git folders** and keeping notebooks under Git version control.

> **Important:** This guide is intended for interactive development and learning. For production CI/CD, Databricks recommends using Declarative Automation Bundles and appropriate workload identity/service-principal patterns where supported.

## 1. Architecture

```text
GitHub Repository
       |
       | HTTPS + Git authentication
       v
Databricks Git Folder
       |
       +--> Notebook 01 - Hello Git
       +--> Notebook 02 - Data Processing
       +--> Notebook 03 - Validation
       |
       v
Databricks Free Edition Workspace
```

The Git folder is the working copy of the repository inside Databricks. You can pull changes from GitHub, edit notebooks, commit changes, and push them back to GitHub.

---

## 2. Prerequisites

You need:

- A Databricks Free Edition workspace.
- A GitHub account.
- A GitHub repository.
- Permission to push to that repository.
- A GitHub authentication method supported by your Databricks workspace.

For a new personal setup, a **fine-grained GitHub personal access token (PAT)** is a good option when PAT authentication is offered. Databricks documentation also recommends the Databricks GitHub App for hosted GitHub accounts where it is available.

### Recommended repository structure

```text
databricks-github-free-edition/
│
├── README.md
├── notebooks/
│   ├── 01_hello_github.py
│   ├── 02_data_processing.py
│   └── 03_data_quality_validation.py
│
├── src/
│   └── README.md
│
└── .gitignore
```

---

# 3. Step 1 — Create the GitHub Repository

1. Sign in to GitHub.
2. Create a new repository.
3. Example repository name:

```text
databricks-github-free-edition
```

4. Set the repository to **Private** if the notebooks contain company/project material.
5. Add a `README.md` if you want GitHub to initialize the repository.

Repository URL example:

```text
https://github.com/<github-username>/databricks-github-free-edition.git
```

Replace `<github-username>` with your GitHub username.

---

# 4. Step 2 — Create GitHub Authentication

## Option A — Databricks GitHub App

If your Databricks Free Edition workspace presents the GitHub App/OAuth authentication option, prefer that option.

The GitHub App can provide scoped access and avoids manually maintaining a long-lived personal token.

Follow the authentication flow presented by Databricks.

## Option B — Fine-Grained Personal Access Token

If PAT authentication is presented in your workspace:

1. Open GitHub.
2. Go to:

```text
Settings
  → Developer settings
  → Personal access tokens
  → Fine-grained tokens
```

3. Select **Generate new token**.
4. Give the token a descriptive name, for example:

```text
databricks-free-edition
```

5. Select an appropriate expiration date.
6. Under **Repository access**, select only the repository that Databricks needs.
7. Grant the minimum repository permissions required for your workflow.
8. Generate the token.
9. Copy the token immediately and store it securely.

### Security rule

Never put the PAT inside:

- A notebook
- `README.md`
- Source code
- `.env` committed to Git
- Screenshots
- Chat messages
- GitHub repository files

Treat the PAT like a password.

---

# 5. Step 3 — Add Git Credentials in Databricks

The Databricks UI can vary slightly by workspace/version, but the current Git integration flow is generally:

```text
Databricks
  → User menu
  → Settings
  → Linked accounts
  → Git integration
  → Add Git credential
```

Select:

```text
Git provider: GitHub
```

If using PAT authentication, provide:

```text
Git provider username/email: <your GitHub username or email>
Token: <your GitHub PAT>
```

Then save the credential.

> Do not type the actual PAT into this README. Enter it only in the Databricks credential UI.

---

# 6. Step 4 — Create a Git Folder

In Databricks:

```text
Workspace
  → Your user/workspace folder
  → Create
  → Git folder
```

Provide:

```text
Git repository URL:
https://github.com/<github-username>/databricks-github-free-edition.git

Git provider:
GitHub
```

Then click **Create Git folder**.

Databricks clones the repository into the Git folder.

You should now see something similar to:

```text
Workspace
└── Users
    └── <your-user>
        └── databricks-github-free-edition
            ├── README.md
            └── notebooks
```

---

# 7. Step 5 — Add a Notebook

Create or import a notebook inside:

```text
notebooks/
```

For example:

```text
notebooks/01_hello_github
```

Paste the content from:

```text
notebooks/01_hello_github.py
```

Run the notebook in Databricks.

The notebook demonstrates that the notebook is being edited from a Git-backed folder.

---

# 8. Step 6 — Commit Changes

After modifying a notebook:

1. Open the Git folder.
2. Open the Git/Source Control panel.
3. Review changed files.
4. Enter a commit message.

Example:

```text
feat: add initial Databricks GitHub notebook
```

5. Commit the changes.
6. Push the commit to GitHub.

Example commit flow:

```text
Databricks notebook
       |
       v
Git folder change
       |
       v
Commit
       |
       v
Push
       |
       v
GitHub
```

---

# 9. Step 7 — Verify on GitHub

Open the GitHub repository in your browser.

You should see:

```text
README.md
notebooks/
    01_hello_github.py
    02_data_processing.py
    03_data_quality_validation.py
```

The commit should also appear in GitHub history.

---

# 10. Step 8 — Pull Changes from GitHub

If another developer changes the repository:

```text
Developer
   |
   v
GitHub
   |
   v
Pull / Update Git folder
   |
   v
Databricks
```

Use the Git folder's pull/update operation to synchronize the Databricks working copy with the remote repository.

Always review local changes before pulling when you have uncommitted work.

---

# 11. Recommended Git Workflow

For a single developer:

```text
main
 |
 +--> edit notebook
 |
 +--> test in Databricks
 |
 +--> commit
 |
 +--> push
```

For a team:

```text
main
 |
 +-----------------------------+
 |                             |
feature/data-pipeline       feature/data-quality
 |                             |
 |                             |
 +------------ PR -------------+
              |
              v
             main
```

Recommended branch names:

```text
feature/<short-description>
bugfix/<short-description>
hotfix/<short-description>
```

Examples:

```text
feature/customer-ingestion
feature/quote-processing
bugfix/schema-validation
```

---

# 12. Suggested Commit Messages

Use clear commit messages.

Good:

```text
feat: add customer ingestion notebook
feat: add data quality validation
fix: handle null customer ids
refactor: simplify transformation logic
docs: update GitHub setup instructions
```

Avoid:

```text
changes
update
test
final
new
abc
```

---

# 13. Notebook Version Control Best Practices

### Keep notebooks small

Instead of one 2,000-line notebook:

```text
01_ingestion
02_transformation
03_validation
04_output
```

### Separate reusable Python code

For larger projects:

```text
src/
    transformations.py
    validations.py
    utilities.py
```

Keep notebooks focused on orchestration, exploration, and execution.

### Do not store secrets

Never do:

```python
github_token = "ghp_xxxxxxxxx"
password = "mypassword"
connection_string = "..."
```

Use Databricks-supported secret management or environment/identity mechanisms appropriate to your workspace.

### Use parameters

Example:

```python
input_path = "/path/to/input"
output_path = "/path/to/output"
```

For production-style projects, make paths and configuration externally configurable.

---

# 14. Common Problems and Fixes

## Problem 1 — Authentication failed

Check:

- GitHub username/email.
- PAT is still valid.
- PAT has access to the selected repository.
- Repository URL is correct.
- Organization policies are not blocking the authentication method.
- If SSO is required by the organization, complete the required authorization.

---

## Problem 2 — Repository cannot be cloned

Check:

```text
Repository URL
       ↓
GitHub repository exists
       ↓
Credential is valid
       ↓
Credential has repository access
       ↓
Databricks Git integration is enabled
```

For a private repository, authentication is required.

---

## Problem 3 — Push is rejected

Possible causes:

- Token does not have sufficient write permission.
- You do not have write access to the repository.
- The remote branch contains commits that your local branch does not have.
- Branch protection rules require a pull request.

Recommended action:

```text
Pull/update
   ↓
Resolve conflicts if required
   ↓
Commit
   ↓
Push
```

---

## Problem 4 — Notebook changes are not appearing in GitHub

Check that you:

1. Saved the notebook.
2. Are working inside the Git folder.
3. Committed the changes.
4. Pushed the commit.
5. Are looking at the correct GitHub branch.

---

# 15. Test Checklist

After setup, verify:

- [ ] GitHub repository created.
- [ ] Git authentication configured.
- [ ] Databricks Git folder created.
- [ ] Repository successfully cloned.
- [ ] Test notebook created.
- [ ] Notebook executed successfully.
- [ ] Change appears in Git status.
- [ ] Change committed.
- [ ] Commit pushed.
- [ ] Commit visible in GitHub.
- [ ] Pull/update tested.
- [ ] Branch workflow tested.

---

# 16. Quick End-to-End Test

Use the following sequence:

```text
1. Create GitHub repository
        ↓
2. Configure GitHub authentication
        ↓
3. Add Git credential in Databricks
        ↓
4. Create Databricks Git folder
        ↓
5. Create 01_hello_github notebook
        ↓
6. Run notebook
        ↓
7. Modify notebook
        ↓
8. Commit
        ↓
9. Push
        ↓
10. Open GitHub
        ↓
11. Verify commit
```

If all ten steps work, your Databricks ↔ GitHub version-control integration is working.

---

# 17. Important Free Edition Notes

Databricks Free Edition is intended for learning, experimentation, and development. Do not assume that capabilities available in a paid Databricks workspace, such as enterprise networking, production deployment controls, or every CI/CD feature, are available in Free Edition.

The exact UI and available authentication choices can change. If your workspace presents a GitHub App/OAuth option, prefer that over manually managing a PAT.

For production environments, use the organization's approved authentication, identity, CI/CD, secret-management, and deployment standards.

---

# 18. Reference Documentation

- Databricks Git folders:
  https://docs.databricks.com/aws/en/repos/repos-setup

- Databricks Git provider authentication:
  https://docs.databricks.com/gcp/en/repos/get-access-tokens-from-git-provider

- Databricks notebook best practices:
  https://docs.databricks.com/gcp/en/notebooks/best-practices

- GitHub personal access tokens:
  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

---

# 19. Project Owner

**Project:** Databricks Free Edition + GitHub Version Control  
**Purpose:** Learning / Development / Notebook Version Control  
**Platform:** Databricks Free Edition  
**Source Control:** GitHub  
**Integration:** Databricks Git folders  
