import os
import subprocess
import shutil
import requests
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

def check_installation(software_name):
    """Check if software is installed."""
    if software_name == "XAMPP":
        return os.path.exists(r"C:\xampp")
    elif software_name == "composer":
        return shutil.which("composer") is not None
    elif software_name == "7zip":
        return shutil.which("7z") is not None
    else:
        return False

def download_and_install(url, installer_name, install_command):
    """Download and install software."""
    try:
        installer_path = f"{installer_name}.exe"
        response = requests.get(url, stream=True)
        with open(installer_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        subprocess.run([installer_path] + install_command, check=True)
        messagebox.showinfo("Installation Complete", f"{installer_name} installed successfully.")
    except Exception as e:
        messagebox.showerror("Installation Error", f"Failed to install {installer_name}: {e}")
    finally:
        if os.path.exists(installer_path):
            os.remove(installer_path)

def extract_project(archive_path, destination_path):
    """Extract project archive."""
    try:
        os.makedirs(destination_path, exist_ok=True)
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(destination_path)
        messagebox.showinfo("Extraction Complete", "Project extracted successfully.")
    except Exception as e:
        messagebox.showerror("Extraction Error", f"Failed to extract project: {e}")

def run_composer_update(destination_path):
    """Run 'composer update' command."""
    try:
        subprocess.run(["cmd", "/c", f"cd /D {destination_path} && composer update"], check=True)
        messagebox.showinfo("Composer Update Complete", "Composer update completed successfully.")
    except Exception as e:
        messagebox.showerror("Composer Update Error", f"Failed to run composer update: {e}")

def install_xampp():
    if not check_installation("XAMPP"):
        download_and_install(
            "https://www.apachefriends.org/xampp-files/7.4.29/xampp-windows-x64-7.4.29-1-VC15-installer.exe",
            "XAMPP",
            ["/S"]
        )
    else:
        messagebox.showinfo("XAMPP Already Installed", "XAMPP is already installed.")

def install_composer():
    if not check_installation("composer"):
        download_and_install(
            "https://getcomposer.org/Composer-Setup.exe",
            "Composer",
            ["/quiet"]
        )
    else:
        messagebox.showinfo("Composer Already Installed", "Composer is already installed.")

def install_7zip():
    if not check_installation("7zip"):
        download_and_install(
            "https://www.7-zip.org/a/7z1900-x64.exe",
            "7zip",
            ["/S"]
        )
    else:
        messagebox.showinfo("7zip Already Installed", "7zip is already installed.")

def browse_archive():
    filename = filedialog.askopenfilename(title="Select Archive File")
    if filename:
        archive_entry.delete(0, tk.END)
        archive_entry.insert(0, filename)

def browse_destination():
    directory = filedialog.askdirectory(title="Select Destination Folder")
    if directory:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, directory)

def start_installation():
    destination_path = destination_entry.get()
    if not os.path.isdir(destination_path):
        messagebox.showerror("Error", "Invalid destination folder.")
        return

    # Create a folder named "BISUBAL_ACSG" in the destination directory
    project_folder_name = "SampleProjectFolder"
    project_folder_path = os.path.join(destination_path, project_folder_name)
    try:
        os.makedirs(project_folder_path, exist_ok=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create project folder: {e}")
        return

    install_xampp()
    install_composer()
    install_7zip()
    extract_project(laravel_project_archive, project_folder_path)
    run_composer_update(project_folder_path)

laravel_project_archive = os.path.join(sys._MEIPASS, "my_project", "SampleLaravelProjectZip.zip")


# Create Tkinter window
root = tk.Tk()
root.title("Installer")

# Create UI components
destination_label = tk.Label(root, text="Destination Folder:")
destination_label.grid(row=0, column=0, sticky="w")
destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=0, column=1)
browse_destination_button = tk.Button(root, text="Browse", command=browse_destination)
browse_destination_button.grid(row=0, column=2)

install_button = tk.Button(root, text="Install", command=start_installation)
install_button.grid(row=1, column=1, pady=10)

# Run Tkinter event loop
root.mainloop()
