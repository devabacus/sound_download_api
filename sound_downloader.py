import requests
import shutil
import time

def download_sound(text, language, output_folder):
    # Step 1: Send a POST request to the API to request the sound file
    url = "https://api.soundoftext.com/sounds"
    data = {
        "engine": "Google",
        "data": {
            "text": text,
            "voice": language
        }
    }

    response = requests.post(url, json=data)
    response_json = response.json()

    if response.status_code == 200:
        print("Request successful, sound ID: ", response_json["id"])
    else:
        print("Error occurred: ", response_json["message"])
        return

    # Step 2: Retrieve the sound file using the sound ID
    sound_id = response_json["id"]
    sound_url = f"https://api.soundoftext.com/sounds/{sound_id}"

    while True:
        response = requests.get(sound_url)
        response_json = response.json()

        if response_json["status"] == "Done":
            download_url = response_json["location"]
            print("Sound file is ready, download URL: ", download_url)
            break
        elif response_json["status"] == "Error":
            print("Error occurred: ", response_json["message"])
            return

        print("Waiting for the sound file to be ready...")
        time.sleep(2)

    # Step 3: Download the sound file and save it locally
    response = requests.get(download_url, stream=True)
    filename = f"{text[:30].replace(' ', '_')}.mp3"

    file_path = f"{output_folder}/{filename}"

    with open(file_path, "wb") as sound_file:
        shutil.copyfileobj(response.raw, sound_file)

    print(f"Sound file successfully downloaded as '{file_path}'")
