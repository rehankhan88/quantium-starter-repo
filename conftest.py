# conftest.py
import os
from webdriver_manager.chrome import ChromeDriverManager

# Automatically download ChromeDriver and add it to PATH
driver_path = ChromeDriverManager().install()
driver_dir = os.path.dirname(driver_path)
os.environ["PATH"] += os.pathsep + driver_dir
