# Lyft Rental Fleet Management System

This repository contains the implementation and unit tests for a rental fleet management system developed for Lyft. The project involves determining when cars in Lyft's rental fleet should be serviced based on various criteria such as engine mileage and battery age.

## Project Overview

The system is designed to handle the service criteria for different car models in Lyft's fleet, taking into account the engine and battery types. The project is divided into several components, each responsible for a specific part of the functionality.

## Installation

To run the project, clone this repository and install the required dependencies.

```bash
git clone https://github.com/Snorman-zzz/Lyft-Backend-Project-in-Forage.git
cd lyft-fleet-management
pip install -r requirements.txt
```

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover
```

## Usage

The system uses a combination of engines and batteries to determine the service criteria for different car models. The current service criteria are as follows:

### Service Criteria

| Engine           | Service Criteria                           |
|------------------|--------------------------------------------|
| Capulet Engine   | Once every 30,000 miles                    |
| Willoughby Engine| Once every 60,000 miles                    |
| Sternman Engine  | Only when the warning indicator is on      |

| Battery          | Service Criteria                           |
|------------------|--------------------------------------------|
| Spindler Battery | Once every 2 years                         |
| Nubbin Battery   | Once every 4 years                         |

### Car Models

| Car Model  | Engine           | Battery          |
|------------|------------------|------------------|
| Calliope   | Capulet Engine   | Spindler Battery |
| Glissade   | Willoughby Engine| Spindler Battery |
| Palindrome | Sternman Engine  | Spindler Battery |
| Rorschach  | Willoughby Engine| Nubbin Battery   |
| Thovex     | Capulet Engine   | Nubbin Battery   |

## Extensibility

The system is designed to be extensible, allowing for the addition of new car models and service criteria. The architecture follows the strategy and factory design patterns to facilitate easy modifications and additions.

---
