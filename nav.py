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


def index_git_repos(search_dirs, output_file="repo_paths.csv"):
    repo_to_path = {}
    for search_dir in search_dirs:
        if search_dir is None or not os.path.isdir(search_dir):
            raise ValueError(f"Error: '{search_dir}' is not a valid directory.")

        for root, dirs, _ in os.walk(search_dir):
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
    dirs = ["~/Dev", "~/.config"]
    search_dirs = [os.path.expanduser(path) for path in dirs]
    output_csv_file = os.path.join(os.getcwd(), "repo_paths.csv")
    repos = index_git_repos(search_dirs, output_csv_file)
    print(f"Indexed {repos} repositories. Done!")
