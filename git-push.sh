#!/bin/bash

# Prompt the user for a commit message
echo "Enter your commit message:"
read commit_message

# Perform the Git commands
git add .
git commit -m "$commit_message"
git push
