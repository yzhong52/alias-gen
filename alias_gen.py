#!/usr/bin/env python3
import os, sys, git
from pathlib import Path

# ~/.alias_gen
alias_gen_file = Path.home().joinpath(".alias_gen") 
# ~/Documents/
workspace = Path.home().joinpath("Documents/")

sys.stdout=open(str(alias_gen_file), "w+")

print("#")
print("# Generated by alia-gen.py")
print("#")

for root, folders, files in os.walk(workspace):
    for folder in sorted(folders):
        try:
            _ = git.Repo(workspace.joinpath(folder)).git_dir # May throw
            alias = ''.join(folder.split()).lower()
            absolute_path=os.path.abspath(os.path.join(root, folder))
            print('alias ' + alias + '="cd ' + absolute_path + '"')
        except git.exc.InvalidGitRepositoryError:
            print("# Skipping directory '" + folder + "' because it is not a git repo")

    # breaking right away since we only care about one level deep
    break
