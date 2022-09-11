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




## Special Thanks to:
Guillaume Rongier for: [https://openexchange.intersystems.com/package/secured-rest-api](https://openexchange.intersystems.com/package/interoperability-embedded-python) template for guidance
