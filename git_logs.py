import subprocess

def show_git_logs():
    try:
        # Run the 'git log' command and capture its output
        result = subprocess.run(['git', 'log'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("Git Logs:\n")
            print(result.stdout)
        else:
            print("Error:", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    show_git_logs()
