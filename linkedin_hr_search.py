import requests
import csv

# Your API credentials
API_KEY = "AIzaSyBbf11gAB-unn68av4W4NV5YTgLabJTyTA"
CX_ID = "b68c430487e9e4cac"

def search_linkedin_hr(company, country, role="HR", num_results=10):
    query = f"site:linkedin.com/in {role} {company} {country}"
    url = "https://www.googleapis.com/customsearch/v1"
    
    params = {
        "q": query,
        "key": API_KEY,
        "cx": CX_ID,
        "num": num_results
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    results = []
    if "items" in data:
        for item in data["items"]:
            title = item.get("title", "")
            link = item.get("link", "")
            
            # Example title: "Ravi Kumar - HR Manager - PwC | LinkedIn"
            parts = title.split("-")
            if len(parts) >= 2:
                name = parts[0].strip()
                position = parts[1].strip()
            else:
                name = title.strip()
                position = ""
            
            # Split name into first and last
            name_parts = name.split()
            first_name = name_parts[0] if len(name_parts) > 0 else ""
            last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
            
            results.append({
                "first_name": first_name,
                "last_name": last_name,
                "position": position,
                "linkedin_url": link
            })
    return results

def save_to_csv(results, filename="linkedin_hr_results.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "position", "linkedin_url"])
        writer.writeheader()
        writer.writerows(results)
    print(f"✅ Results saved to {filename}")

if __name__ == "__main__":
    company = input("Enter company name: ")  # e.g., PwC, EY, Infosys
    country = input("Enter country name: ")  # e.g., India, US
    results = search_linkedin_hr(company, country, role="HR", num_results=10)
    
    if results:
        for r in results:
            print(r)
        save_to_csv(results)
    else:
        print("No results found.")
