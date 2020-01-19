import requests

def get_data(lenght, width):
    request = requests.get(
        f'https://api.darksky.net/forecast/7c53a90481bcc12e69c188a374ddae2d/{lenght},{width}')
    data = request.json()

    main_data = data['currently']
    print(main_data)
    return main_data


