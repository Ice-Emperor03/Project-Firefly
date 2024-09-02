import requests


def get_ngrok_url():
    try:
        # Make a request to the ngrok API
        response = requests.get('http://localhost:4040/api/tunnels')
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        tunnels = response.json().get('tunnels', [])

        # Check if there are any tunnels
        if not tunnels:
            print('No active ngrok tunnels found.')
            return None

        # Return the public URL of the first tunnel found
        for tunnel in tunnels:
            public_url = tunnel.get('public_url')
            stripped_url = public_url.replace('https://', '')
            return stripped_url

        # Return None if no valid public URL is found
        print('No valid public URL found in the active ngrok tunnels.')
        return None

    except requests.RequestException as e:
        print(f'Error accessing ngrok API: {e}')
        return None
