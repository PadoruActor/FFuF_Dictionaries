import subprocess

def run_ffuf(wordlist, url):
    try:
        result = subprocess.run(
            ['ffuf', '-w', wordlist, '-u', url],
            capture_output=True,
            text=True,
            check=True
        )
        # Print both stdout and stderr
        print("FFUF Output:")
        print(result.stdout)
        print(result.stderr)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"FFUF failed with error: {e.stderr}")
        return None

# Usage
wordlist = r"C:\Users\Vyacheslav\PycharmProjects\FFuF_Trainee\Dicts\DB&SQLInj\OracleDB-SID.txt"
target_url = "http://guap.ruFUZZ"
run_ffuf(wordlist, target_url)