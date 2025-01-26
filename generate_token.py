from google_auth_oauthlib.flow import InstalledAppFlow

# Specify the scopes your app needs
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']

def generate_token():
    # Path to the credentials.json file you downloaded
    credentials_file = 'credentials.json'
    
    # Start the authentication flow
    flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
    creds = flow.run_local_server(port=0)
    
    # Save the credentials to token.json
    with open('token.json', 'w') as token_file:
        token_file.write(creds.to_json())
    print("Token.json file generated successfully!")

if __name__ == "__main__":
    generate_token()
