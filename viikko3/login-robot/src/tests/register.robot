*** Settings ***
Resource  resource.robot
Test Setup  Initialize tests

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  peruna  salasana
    Output Should Contain  New user registered
    

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  porkkana  kalasana
    Output Should Contain  User with username porkkana already exists
    

# Register With Too Short Username And Valid Password
#     # ...

# Register With Valid Username And Too Short Password
#     # ...

# Register With Valid Username And Long Enough Password Containing Only Letters
#     # ...


*** Keywords ***
Initialize tests
    Create User  porkkana  salasana