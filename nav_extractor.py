import requests
import json

def fetch_nav_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_scheme_asset(nav_text):
    lines = nav_text.splitlines()
    data = []
    start = False
    for line in lines:
        if "Scheme Code" in line:
            start = True
            continue
        if start and line.strip():
            fields = line.split(';')
            if len(fields) >= 5:
                scheme_name = fields[3].strip()
                asset_value = fields[4].strip()
                data.append({
                    "Scheme Name": scheme_name,
                    "Asset Value": asset_value
                })
    return data

def save_as_tsv(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item['Scheme Name']}\t{item['Asset Value']}\n")

def save_as_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def main():
    url = "https://www.amfiindia.com/spages/NAVAll.txt"
    print("Downloading NAV data...")
    nav_text = fetch_nav_data(url)

    print("Extracting Scheme Name and Asset Value...")
    extracted_data = extract_scheme_asset(nav_text)

    tsv_file = "scheme_asset_data.tsv"
    json_file = "scheme_asset_data.json"

    print(f"Saving data to {tsv_file}...")
    save_as_tsv(extracted_data, tsv_file)

    print(f"Saving data to {json_file}...")
    save_as_json(extracted_data, json_file)

    print("Data extraction complete.")

if __name__ == "__main__":
    main()