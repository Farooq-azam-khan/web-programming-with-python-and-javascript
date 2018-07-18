# Testing, CI/CD
- testing is helpful to not break huge projects
- `prime.py`
- `assert` a value to tell if value is true or false
  - see: `assert0.py`, `assert1.py`
  
## unittest module
- see: `test1.py`

## test.py file in django
- see: `airline1/test.py`
- `python manage.py test`
- should also test templates in django as well, see: `airline2/`
- 'Client' class will simulate a client
- `assertNotEqual`, `assertIn`, `assertNotIn`, etc. 

## Testing JS apps
- Selenium is a tool for testing JS apps because Django testing is for server side
- pretends to be user

## Travis CI
### YAML
  - like a json or dict:
    - ```
    key1:value1
    key2:value2
    key3:
        -listval0
        -listval1
        -listval2
        - ...
      ...
    ```
- yaml for travis: 
```
language: python 
python: 
      - 3.6
install: 
      - pip install -r requirements.txt
script:
    - python manage.py test
```