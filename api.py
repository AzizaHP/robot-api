*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_url}     https://reqres.in/

*** Keywords ***
#GET
get single user
    Create Session     mysession   ${base_url}  verify=true
    #${response}=         get on session     mysession   api/users/2

validations user
    ${response}=        get on session     mysession   api/users/2
    ${status_code}=     convert to string   ${response.status_code}
    should be equal     ${status_code}      200
    log to console      ${status_code}

show data user
    ${response}=         get on session     mysession   api/users/2
    ${body}=            convert to string   ${response.content}
    should contain      ${body}             Janet
    log to console      ${body}

#POST
post user
    Create Session     mysession   ${base_url}  verify=true

create user
    ${body}=     create dictionary   name=morpheus   job=leader
    ${header} =    create dictionary    Content-Type=application/json
    ${response}=    post request    mysession   api/users    data=${body}    headers=${header}

    #validations
    ${status_code}=    convert to string    ${response.status_code}
    should be equal    ${status_code}    201

    log to console    ${response}
    log to console    ${response.content}
    log to console    ${response.status_code}

*** Test Case ***
Get Single User
    Given get single user
    When validations user
    Then show data user
Post Create User 
    Given post user
    When create user