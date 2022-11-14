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
    Input Credentials  pe  salasanaT5
    Output Should Contain  Username must have 3 characters and contain only letters a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  peruna  S4a!la
    Output Should Contain  Password must have 8 characters and can not only have letters.


# Erilainen tapa testata käyttäjävirhe. Opiskelin Robot Frameworkin dokumentaatiosta
Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Run Keyword And Expect Error  UserInputError: Password must have 8 characters and can not only have letters.  Password With Only Letters


*** Keywords ***
Initialize tests
    Create User  porkkana  salasanaT5

Password With Only Letters
    Create User  peruna  salasanA