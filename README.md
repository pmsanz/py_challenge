# py_challenge
Interview Challenge Repository in Python

API Rest to get dataset information. By request filters.

**Only for testing propouse**

### Table of Contents
* **[Installation](#Installation)**
* **[Overview](#Overview)**
   * **[Usage](#Usage)**
   * **[Validated Data/Error Messages](#Messages)**
   * **[Results](#Results)**
   * **[Available Validation Rules](#Available-Validation-Rules)**
* **[Developer](#Developer)**
* **[Information](#Information)**

<a name="Installation"></a>
## Installation

Use the package manager [pip](https://pypi.org/project/flask/) to install Flask.
Use the package manager [pip](https://pypi.org/project/jsonify/) to install jsonfy.
Use the package manager [pip](https://pypi.org/project/validator/) to install Validator.

```bash
pip install validator
pip install falsk
pip install jsonfy
```

<a name="Overview"></a>

<a name="Usage"></a>
## Usage && Example of use

User should pass request "POST" for send filter data in the request.

Please see examples below:

|Variable Name  |Default url value               |Set in         |TYPE  |Example|
|----------|----------------------------|---------------|-----------------|-------|
|`Defaul Url`|`http://localhost:5000/getFiltered/`|url    |- Environment               |-      |
|`indicator`|`http://localhost:5000/getFiltered/` |Form-Data     |String      |`SW_LIFS`|
|`value`|`http://localhost:5000/getFiltered/` |Form-Data     |Decimal      |`5.5`|

<a name="Messages"></a>
## Validated Data/Error Messages
This API allows user to have a look at failed message for invalid parameters: **"Please enter valid parameters"**
Default rule = 
**indicator must be at minimun lenght of 7 and is required**
**value must be Decimal casteable, minimun value at 0 and required**

You can set the min variable to allow or deny requests, modifying rules validations:

* Basic data validator rules:

    ```python
   rule = {"indicator": [R.Required(), R.Min(7)],
            "value": [R.Required(), R.Min(0)]}
    
    ```

<a name="Results"></a>
## Results
When you gives to API, one CORRECT POST. Returns an JSON with next parameters:
```json
{
"status":"OK"
"message": {
        "0": [
            "\"Australia\"",
            "7.3"
        ],
        "1": [
            "\"Austria\"",
            "7"
          ]
		}
}
```		
When you gives to API, one WRONG POST. Returns an JSON with next parameters:

```json
{
    "message": "Please enter valid parameters",
    "status": "error"
}
```
<a name="Developer"></a>
## Developed by
Pablo Matias Sanz : https://www.linkedin.com/in/pablo-sanz-67907056/

<a name="Information"></a>
## More Repos
Some IA projects on python: https://github.com/pmsanz/IA.git
 
