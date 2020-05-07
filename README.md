# Djangoino

WebApp that fetch data from a sensor connected in arduino
and the plot the gatherd data in a Chartplot.

## Installation
In your [venv](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
python -m pip install -r requirements.txt
```

## Setting
**In your venv do**
```python
(venv)  python manage.py migrate 
(venv)  python manage.py makemigration application 
(venv)  python manage.py migrate application 
(venv)  python manage.py runserver
```
**In Aruino**

```Arduino
Install arduino required libraries 
Change Credential acording to in Arduino Sketch
Upload Sketch to Arduino(NodeMCU)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2020 Ranger Geronimo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

