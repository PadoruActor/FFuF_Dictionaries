import subprocess


def run_ffuf(wordlist, url):
    # Ensure URL contains FUZZ
    if "FUZZ" not in url:
        url = url.rstrip("/") + "FUZZ"

    try:
        result = subprocess.run(
            ['ffuf', '-w', wordlist, '-u', url],
            capture_output=True,
            text=True,
            check=True
        )
        print("FFUF Output:")
        print(result.stderr)  # Progress info
        print(result.stdout)  # Results
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"FFUF failed with error: {e.stderr}")
        return None


# Usage
wordlist = r"C:\Users\Vyacheslav\PycharmProjects\FFuF_Trainee\Dicts\DBSQLInj\MSSQL-Enumeration.fuzzdb.txt"
#DICT
#


target_url = "http://guap.ru"  # FUZZ will be added automatically
print(f"ffuf -w {wordlist} -u {target_url}FUZZ ")






#run_ffuf(wordlist, target_url)