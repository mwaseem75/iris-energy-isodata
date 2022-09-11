![image](https://user-images.githubusercontent.com/18219467/189523406-1da330b7-080b-4a06-95f5-701cbe1e21d3.png)

iris_isodata app access energy data from the major Independent System Operators (ISOs) in the United States.

Currently supports fuel mix, load, supply, load forecast, and LMP pricing data for CAISO, SPP, ISONE, MISO, Ercot, NYISO, and PJM. See full availability below.

This proof of concept aims to show how the **iris interoperability framework** can be use with **embedded python**.


## Features
* Get Fuel Mix
* Get Today Forecast, Demand and supply
* Get Latest Demand and Supply
* Get Historical Demand and supply

## List of Independent systems operators(ISOs) 
* California ISO (caiso)
* Electric Reliability Council of Texas (ercot)
* New York ISO (nyiso)
* Southwest Power Pool (spp)
* PJM (pjm)
* Midcontinent ISO (miso)
* ISO New England (isone)

## Medthods Availability
![image](https://user-images.githubusercontent.com/18219467/189523605-52527d0d-6f8e-433e-9506-f46a01a26138.png)

## Repo Contents   
* Dockerfile, docker-compose.yml, and Installer.cls to create container
* iris.script, contains script to execute during container initialization 
* /src with source files 
* /.vscode/settings.json for automatic server connections when opened in VS Code.

## Requirements:  
* [Docker desktop]( https://www.docker.com/products/docker-desktop)
* Get the latest InterSystems IRIS for Health image for use in the Dockerfile: https://hub.docker.com/_/intersystems-iris-for-health  

## To Run on Windows:  
```
	git clone https://github.com/mwaseem75/Data_APP_Security.git  
	cd Data_APP_Security  
	docker-compose up -d  
```
## To Run on macOS:  

```
	git clone https://github.com/mwaseem75/Data_APP_Security.git 
	cd Data_APP_Security 
	docker-compose up -d  
```
Log in with credentials: SuperUser | SYS

## Getting Started 

## AUTHENTICATION
* Navigate to http://localhost:52773/csp/user/index.csp index page, First of all create New user by cliking "Create TestUser" button. Make sure to login as SUPERUSER OR _SYSTEM in order to create new User.
Newly created user can be viewed from management portal (System > Security Management > User)
![image](https://user-images.githubusercontent.com/18219467/143899649-a1f630de-fff5-4e08-ae11-30185c83b718.png)

## LOGIN With Github OAUTH2
![image](https://user-images.githubusercontent.com/18219467/144722058-47423b00-f862-4e21-811b-316e7becc684.png)
* 1-Navigate to online Demo https://dappsecurity.demo.community.intersystems.com/csp/user/index.csp by using SuperUser | SYS
* 2-Select menu option "Login with Github account" 
* 3-Enter your github credentials in Github login screen
* 4-For details see the article : https://community.intersystems.com/post/oauth2-authentication-github-account-iris-web-application


# Credits
## Special Thanks to:
Guillaume Rongier for: [https://openexchange.intersystems.com/package/secured-rest-api](https://openexchange.intersystems.com/package/interoperability-embedded-python) template for guidance
