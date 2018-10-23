*** Settings ***
Library  SeleniumLibrary
#Library  allure
#Library  AllureReportLibrary    C:\\Development\\robot-scripts\\FinalTests\\Results\\Allure
*** Variables ***

*** Keywords ***

*** Test Cases ***
TC12
    Open browser  https://www.google.com  chrome
    log to console  TestOK

