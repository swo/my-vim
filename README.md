# My vimrc

This repo helps bootstrap my vim setup, including:

- `.vimrc` file
- list of packages
- Script to symlink the `.vimrc` file and package directory to this repo's vimrc and package directory
- Script to download the packages in the package list

## Getting started

- Run `setup-links.py` to symlink your `~/.vimrc` and package directory to this repo's vimrc and package directory
- Run `download-packages.py` to download the packages in the package list
- Run `get-package-list.py` to produce a JSON of the currently-installed packages

## Usage

Make sure to download new packages to this `start/` folder, *not* the `~/.vim/` folder structure
