#!/usr/bin/env python3

import os, os.path, configparser, json

def get_url(fn):
    c = configparser.ConfigParser()
    c.read(fn)
    return c['remote "origin"']["url"]

base_path = "start"
dir_names = os.listdir(base_path)
config_paths = [os.path.join(base_path, x, ".git", "config") for x in dir_names if x != ".placeholder"]
urls = [get_url(x) for x in config_paths]

data = {dir_name: url for dir_name, url in zip(dir_names, urls)}

print(json.dumps(data, indent=2))
