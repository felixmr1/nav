import csv
import os

skip_dirs = [
    "node_modules",
    "venv",
    "env",
    "__pycache__",
    ".git",
    ".local",
    ".cache",
    ".gvm",
    ".terraform",
    ".dotfiles",
]


def clean_path(path):
    """Clean path by removing any carriage returns and normalizing separators"""
    return os.path.normpath(path.strip().replace("\r", ""))


def index_git_repos(search_path, output_file="repo_paths.csv"):
    if search_path is None or not os.path.isdir(search_path):
        raise ValueError(f"Error: '{search_path}' is not a valid directory.")

    repo_to_path = {}
    for root, dirs, _ in os.walk(search_path):
        if ".git" in dirs:
            repo = os.path.basename(root)
            repo_to_path[repo] = clean_path(root)
            dirs.clear()
        else:
            for skip_dir in skip_dirs:
                if skip_dir in dirs:
                    dirs.remove(skip_dir)

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        for key, value in repo_to_path.items():
            writer.writerow([clean_path(key), clean_path(value)])

    return len(repo_to_path)


if __name__ == "__main__":
    search_dir = os.path.expanduser("~/Dev")
    output_csv_file = os.path.join(os.getcwd(), "repo_paths.csv")
    repos = index_git_repos(search_dir, output_csv_file)
    print(f"indexed {repos} repositories.. Done!")
