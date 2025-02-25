#!/usr/bin/env python3

import os
import os.path


def create_symlink(dst, src, debug=False):
    """
    Beware that dst is the path of the symlink, and src is where it points:
    # os.symlink(src, dst, target_is_directory=False, *, dir_fd=None)
    # Create a symbolic link pointing to src named dst.
    """
    # Check if the symbolic link exists
    exists = os.path.exists(dst)
    islink = os.path.islink(dst)

    if exists and not islink:
        raise RuntimeError(f"{dst} is already a non-symlinked file. Delete it.")
    elif exists and islink:
        actual_src = os.readlink(dst)
        if actual_src == src:
            print(f"{dst} symlink exists and correctly points to {src}")
        else:
            raise RuntimeError(
                f"{dst} is symlinked to {actual_src}, not {src}. Delete it."
            )
    elif not exists:
        print(f"Symlink {dst} -> {src}")
        if not debug:
            os.symlink(src, dst)
    else:
        raise RuntimeError("Bad symbolic link check")


if __name__ == "__main__":
    # Create the .vimrc link
    create_symlink(os.path.expanduser("~/.vimrc"), os.path.abspath(".vimrc"))

    # Create the folder structure to place the package folder
    package_dir_parent = os.path.expanduser("~/.vim/pack/plugins")
    if os.path.exists(package_dir_parent):
        print(f"Package directory parent {package_dir_parent} exists")
    else:
        os.makedirs(package_dir_parent)
        print(f"Package directory parent {package_dir_parent} created")

    # Create the package folder symlink
    create_symlink(
        os.path.expanduser("~/.vim/pack/plugins/start"), os.path.abspath("start")
    )
