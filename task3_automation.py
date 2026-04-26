"""
CodeAlpha Internship - Task 3: Task Automation with Python Scripts
Author: CodeAlpha Intern
Description: Automates three real-life repetitive tasks:
  1. Move all .jpg files from a folder to a new folder
  2. Extract all email addresses from a .txt file
  3. Scrape the title of a fixed webpage
"""

import os
import re
import shutil


# ─────────────────────────────────────────────
# AUTOMATION 1: Move .jpg Files to a New Folder
# ─────────────────────────────────────────────

def move_jpg_files(source_folder=".", destination_folder="jpg_files"):
    """
    Move all .jpg files from source_folder to destination_folder.
    Creates the destination folder if it doesn't exist.
    """
    print("\n" + "=" * 50)
    print("  📁 AUTOMATION 1: Move JPG Files")
    print("=" * 50)

    if not os.path.exists(source_folder):
        print(f"  ❌ Source folder '{source_folder}' does not exist.")
        return

    # Create destination if not exists
    os.makedirs(destination_folder, exist_ok=True)

    jpg_files = [f for f in os.listdir(source_folder)
                 if f.lower().endswith(".jpg") and os.path.isfile(os.path.join(source_folder, f))]

    if not jpg_files:
        print(f"  ⚠  No .jpg files found in '{source_folder}'.")
        return

    moved = 0
    for filename in jpg_files:
        src = os.path.join(source_folder, filename)
        dst = os.path.join(destination_folder, filename)
        shutil.move(src, dst)
        print(f"  ✅ Moved: {filename}  →  {destination_folder}/")
        moved += 1

    print(f"\n  Done! {moved} file(s) moved to '{destination_folder}/'.")


# ─────────────────────────────────────────────────────────
# AUTOMATION 2: Extract Email Addresses from a .txt File
# ─────────────────────────────────────────────────────────

def extract_emails(input_file="input_emails.txt", output_file="extracted_emails.txt"):
    """
    Extract all email addresses from input_file using regex,
    and save unique emails to output_file.
    """
    print("\n" + "=" * 50)
    print("  📧 AUTOMATION 2: Extract Email Addresses")
    print("=" * 50)

    if not os.path.exists(input_file):
        # Create a sample input file for demo purposes
        print(f"  ℹ  '{input_file}' not found. Creating a sample file for demo...\n")
        sample_text = """
        Hello team,
        Please contact john.doe@example.com or jane_smith@gmail.com for details.
        For billing, reach out to billing@codealpha.tech or support@codealpha.tech.
        Duplicate test: john.doe@example.com
        Invalid emails like @noname.com or missing@.com are ignored.
        Also reach: intern2024@yahoo.co.in and hr_team@company.org
        """
        with open(input_file, "w") as f:
            f.write(sample_text)
        print(f"  ✅ Sample file '{input_file}' created.")

    with open(input_file, "r") as f:
        content = f.read()

    # Regex pattern for valid email addresses
    email_pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(emails))

    if not unique_emails:
        print("  ⚠  No email addresses found.")
        return

    print(f"\n  Found {len(unique_emails)} unique email(s):\n")
    for email in unique_emails:
        print(f"    • {email}")

    with open(output_file, "w") as f:
        f.write("Extracted Email Addresses\n")
        f.write("=" * 40 + "\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"\n  ✅ Saved to '{output_file}'.")


# ─────────────────────────────────────────────────────
# AUTOMATION 3: Scrape Title of a Fixed Webpage
# ─────────────────────────────────────────────────────

def scrape_webpage_title(url="https://www.python.org", output_file="scraped_title.txt"):
    """
    Scrape the <title> tag of a webpage and save it to a file.
    """
    print("\n" + "=" * 50)
    print("  🌐 AUTOMATION 3: Scrape Webpage Title")
    print("=" * 50)

    try:
        import urllib.request
        print(f"\n  Fetching: {url} ...")

        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")

        # Extract title using regex (no external library needed)
        match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            print(f"\n  ✅ Page title found:\n     \"{title}\"")

            with open(output_file, "w") as f:
                f.write(f"URL   : {url}\n")
                f.write(f"Title : {title}\n")
            print(f"\n  ✅ Saved to '{output_file}'.")
        else:
            print("  ⚠  Could not find a <title> tag on the page.")

    except Exception as e:
        print(f"  ❌ Error fetching page: {e}")
        print("  ℹ  Check your internet connection and try again.")


# ─────────────────────────────────────────────
# MAIN MENU
# ─────────────────────────────────────────────

def main():
    print("=" * 50)
    print("   🤖 TASK AUTOMATION — CodeAlpha Internship")
    print("=" * 50)
    print("\n  Choose an automation to run:\n")
    print("  1. Move all .jpg files to a new folder")
    print("  2. Extract emails from a .txt file")
    print("  3. Scrape title of a webpage")
    print("  4. Run ALL automations")
    print("  0. Exit")

    while True:
        choice = input("\n  Enter your choice (0-4): ").strip()

        if choice == "1":
            src = input("  Source folder path (press Enter for current): ").strip() or "."
            dst = input("  Destination folder name (press Enter for 'jpg_files'): ").strip() or "jpg_files"
            move_jpg_files(src, dst)
        elif choice == "2":
            inp = input("  Input .txt file (press Enter for 'input_emails.txt'): ").strip() or "input_emails.txt"
            out = input("  Output file (press Enter for 'extracted_emails.txt'): ").strip() or "extracted_emails.txt"
            extract_emails(inp, out)
        elif choice == "3":
            url = input("  Webpage URL (press Enter for 'https://www.python.org'): ").strip() or "https://www.python.org"
            scrape_webpage_title(url)
        elif choice == "4":
            move_jpg_files()
            extract_emails()
            scrape_webpage_title()
        elif choice == "0":
            print("\n  Goodbye! 👋")
            break
        else:
            print("  ⚠  Invalid choice. Please enter 0–4.")


if __name__ == "__main__":
    main()
