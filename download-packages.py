#!/usr/bin/env python3

import json, os.path, subprocess

def download_package(package_name, package_url, target_dir, debug=False):
    path = os.path.join(target_dir, package_name)
    command = ["gh", "repo", "clone", package_url, path]

    if debug:
        print(command)
    else:
        subprocess.run(command)

# read in list of packages
with open("package-list.json") as f:
    package_list = json.load(f)

# check which ones already exist
start_path = "start/"
existing_packages = os.listdir(start_path)
needed_packages = [x for x in package_list if x not in existing_packages]

print("Packages to download:")
print(*needed_packages, sep="\n")

# clone the missing ones
for package in needed_packages:
    download_package(package, package_list[package], start_path)
