login_id="SB284"
password="#$Iitdelhi88"
Totp=""

try:
    access_token=open("access_token.txt","r").read().rstrip()
except Exception as e:
    print("Exception occured")
    access_token=None