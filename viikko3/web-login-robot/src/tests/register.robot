*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  peruna
    Set Password  peruna123
    Confirm Password  peruna123
    Submit Credentials
    Register Should Succeed


Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  peruna123
    Confirm Password  peruna123
    Submit Credentials
    Register Should Fail With Message  Username must have 3 characters and contain only letters a-z


Register With Valid Username And Too Short Password
    Set Username  peruna
    Set Password  perUn4
    Confirm Password  perUn4
    Submit Credentials
    Register Should Fail With Message  Password must have 8 characters and can not only have letters.


Register With Nonmatching Password And Password Confirmation
    Set Username  peruna
    Set Password  perUn444
    Confirm Password  perUn445
    Submit Credentials
    Register Should Fail With Message  Passwords do not match!


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

# Create User And Go To Login Page
#     Create User  kalle  kalle123
#     Go To Login Page
#     Login Page Should Be Open
