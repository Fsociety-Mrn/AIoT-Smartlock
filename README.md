# MGA GAGAWIN AT DAPAT GAWIN

## Login interface
* Signup
    - Don't have an account ? <Strong> Request Now </Strong>   
    pagclinick mapupunta sa signup pages
    - Sign Up pages
        - pero i login muna OTP,   
        - after setup email ,password and confirm password
        - setup Prfile (Optional)
        - Setup First Name and Last Name
        - setup username
        - setup password for locker


## Admin Account 

* Analytics Dashboard
NOTE: meron si Firebase analytics  
    - User Activity Reports
    - who recently access the locker within that day

* My Locker
  - unlock the smart lock
  - Generate token for updated faces
  - change locker

* Profile Settings
  - Profile Information: Allow users to update their personal information such as name, contact details, and  preferred communication methods.
  - change Info
  - change password
  - logout

* Check Availability
  - check the locker availability
  - check if the locker is open or not (pwede optional)

* Manage Locker Access
  - List of registered faces
    - for each locker check if user is active
  - generate OTP token user
  - view the generate Token
* Settings and Configuration
  - check if Raspbery is Online (Indicator)
  - adjust if need to updated the website

## User Account 
* My Locker
    - generate for updating the user
* History
    - when they access the locker
* Account Settings
    - set for active nad inactive
    - delete account
    - logout

# PAANO IDEPLOY SA WEBSITE ?

* login mo muna yung AIoTSmartlock gmail  account sa browser mo
* optional to run moto
```shell
firebase logout
```
tapos ilogin moyung AIoTSmartlock gmail 
```shell
firebase login
```
* run this code 
```shell
npm run build
```
* para mag deploy sa website natin
```shell
firebase deploy
```
