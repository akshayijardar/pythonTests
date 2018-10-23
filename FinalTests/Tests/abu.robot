*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
TestCaseAbu
    Open Browser  https://mail.google.com  chrome
    log to console  TestOK