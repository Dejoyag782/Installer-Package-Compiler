# InstallerPackageCompiler
A python program that creates an installer of a laravel project encased in a zip file. It checks for missing basic requirements in order for a laravel application to function in windows such as XAMPP, Composer, &amp; 7zip.


In order to execute you must first install python

after installing python run a console and execute this command "pip install pyinstaller"

Place your application zip file in the "my_project" folder and update the "installer_withUI.spec" and "installer_withUI.py" and look for the zip file name

once done you can proceed to opening a terminal on the InstallerPackageCompiler directory and execute "pyinstaller installer_withUI.spec"

after the compiler is done you can now use the installer executable file found in the "dist" folder inside the InstallerPackageCompiler directory.
