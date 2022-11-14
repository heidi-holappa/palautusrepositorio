*** Settings ***
Resource  resource.robot
Test Setup  Initialize tests

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  peruna  salasanaT5
    Output Should Contain  New user registered
    

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  porkkana  kalasanaT5
    Output Should Contain  User with username porkkana already exists
    

Register With Too Short Username And Valid Password
    Input New Command
    Run Keyword And Expect Error  UserInputError: Username must have 3 characters and contain only letters a-z  Too Short Username
    # Create User  pe  salaS4na
    # Output Should Contain  Username must have 3 characters and contain only letters a-z

# Register With Valid Username And Too Short Password
#     # ...

# Register With Valid Username And Long Enough Password Containing Only Letters
#     # ...


*** Keywords ***
Initialize tests
    Create User  porkkana  salasanaT5

Too Short Username
    Create User  pe  salasanaT5