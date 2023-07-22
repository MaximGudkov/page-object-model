<h1 align="center">Project about testing with Python, Pytest and Selenium using Page Object Model</h1>
<p>You can clone this repository and run any test from <strong>test_main_page.py</strong> or <strong>test_product_page.py</strong> it will be interesting</p>
<h2>How to run it:</h2>
<h4>2 parametrs:</h4>
<pre><li>language      |  "pytest --language=es [file_name]"           |   apply: "ru" (default); "en"; "fr"...</li></pre>
<pre><li>browser_name  |  "pytest --browser_name=firefox [file_name]"  |  apply: "chrome" (default); "firefox"</li></pre>
<h4>6 marks (only 4 used yet):</h4>
<pre><li>"pytest -m xfail [file_name]"  |  apply: look at pytest.ini file</li></pre>
<h4>Other commands:</h4>
<pre><li>"pytest -v [file_name]" - leaves detailed test results</li></pre>
<pre><li>"pytest -s [file_name]" - see the text that is output using print</li></pre> 
<pre><li>"pytest --tb=line [file_name]" - output only one line to the log of each failed test</li></pre>
<p></p>
<h4>Examples:</h4>
<pre><li>"pytest -v --language=en --browser_name=firefox test_main_page.py"
- Will run all tests in test_main_page.py using firefox browser and english language,
and also will leave detailed test results</li></pre>
<pre><li>"pytest -m xfail --language=es test_product_page.py"
- Will run all tests that are marked 'xfail' in test_product_page.py using chrome browser
and spanish language</li></pre>
<pre><li>"pytest --tb=line test_product_page.py"
- Will run all tests in test_product_page.py using chrome browser and english language,
and also will output only one line to the
log if test has fallen</li></pre>
<h2>Good luck and have fun!!!</h2>
<img src="https://media.tenor.com/Z73zwxJhLpsAAAAi/cat.gif" width="256" height="256" alt="Cat Sticker - Cat Stickers">
