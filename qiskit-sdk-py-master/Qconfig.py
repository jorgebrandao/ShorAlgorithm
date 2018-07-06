# Before you can use the jobs API, you need to set up an access token.
# Log in to the Quantum Experience. Under "Account", generate a personal 
# access token. Replace "None" below with the quoted token string.
# Uncomment the APItoken variable, and you will be ready to go.

APItoken = "db0a4301ed91166b3473413cfc0c86b0e2be61b98caf7a5af6b59a3ba5a9c888ef315acfb610e54dde3ff3e6384243da133c04908b6a1427e058a2512a53227a"

config = {
  "url": 'https://quantumexperience.ng.bluemix.net/api'
}

if 'APItoken' not in locals():
  raise Exception("Please set up your access token. See Qconfig.py.")
