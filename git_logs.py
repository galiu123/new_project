import subprocess

def display_git_logs(/home/galiu/git_project/):
    try:
        # Navigate to the specified repository path
        result = subprocess.run(
            ['git', '-C', /home/galiu/git_project/, 'log', '--oneline', '--graph', '--decorate'],
            text=True,
            capture_output=True,
            check=True
        )

        # Print the captured Git logs
        print(f"Git logs for repository at '{/home/galiu/git_project/th}':\n")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
    except FileNotFoundError:
        print("Git is not installed or the specified repository path is invalid.")

if __name__ == "__main__":
    # Specify the path to your Git repository here
    /home/galiu/git_project/ = "/path/to/your/repository"
    display_git_logs(/home/galiu/git_project/)
