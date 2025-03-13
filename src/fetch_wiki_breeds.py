import requests

def get_wiki_breed_summary(breed_name):
    page_title = breed_name.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            'title': data.get('title', ''),
            'description': data.get('description', ''),
            'extract': data.get('extract', ''),
            'thumbnail': data.get('thumbnail', {}).get('source', ''),
            'original_image': data.get('originalimage', {}).get('source', '')
        }
    return {}
