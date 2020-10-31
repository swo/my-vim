#!/usr/bin/env python3

import json, os.path, subprocess

# read in list of packages
with open("package_list.json") as f:
    package_list = json.load(f)

# check which ones already exist
start_path = "/home/swo/.vim/pack/swo/start"
existing_packages = os.listdir(start_path)
needed_packages = [x for x in package_list if x not in existing_packages]

print(needed_packages)

# clone the missing ones
for package in needed_packages:
    target = os.path.join(start_path, package)
    command = ["gh", "repo", "clone", package_list[package], target]
    subprocess.run(command)
