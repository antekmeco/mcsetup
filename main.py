import getpass
import os
import tarfile

import requests

username = getpass.getuser()


def main():
    print(f"Welcome {username}")
    engine = input("Select your engine > ")
    match engine:
        case 'cuberite':
            cuberite()
        case 'paper':
            paper()


def paper():
    global mcdir
    mcdir = input("Where do you want to install the server? > ")
    os.mkdir(mcdir)
    print("Avaible versions")
    print("1.19")
    print("1.18.2")
    version = input("Select your version > ")
    match version:
        case '1.19':
            open(f"{mcdir}/paper.jar", "wb").write(
                requests.get("https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/386/downloads/paper-1"
                             ".18.2-386.jar").content)

            papersetup()

        case '1.18.2':
            open("/tmp/cuberite.tar.gz", "wb").write(
                requests.get("https://download.cuberite.org/linux-x86_64/Cuberite.tar.gz").content)


def cuberite():
    mcdir = input("Where do you want to install the server? > ")
    open("/tmp/cuberite.tar.gz", "wb").write(
        requests.get("https://download.cuberite.org/linux-x86_64/Cuberite.tar.gz").content)
    print("Downloading")
    tarfile.open('/tmp/cuberite.tar.gz').extractall(path=f'{mcdir}')
    print(f"Installed to {mcdir}")
    chpw = input("Do you want to change your password? > y/n ")
    if chpw == "y":
        pw = input("write your password here > (will echo) ")
        with open(f"{mcdir}/webadmin.ini", "w") as f:
            f.write("[User:admin]\n")
            f.write(f"password={pw}\n")

    run = input("Do you want to run now? > y/n")
    os.chdir(f"/home/{username}/mc/")
    if run == "y":
        os.system(f"{mcdir}/Cuberite")
    os.remove("/tmp/cuberite.tar.gz")


def papersetup():
    global mcdir
    open(f"{mcdir}/java.tar.gz", "wb").write(
        requests.get(
            "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.3%2B7/OpenJDK17U-jdk_x64_linux_hotspot_17.0.3_7.tar.gz").content)
    tarfile.open(f'{mcdir}/java.tar.gz').extractall(path=f'{mcdir}')
    os.rename(f"{mcdir}/jdk-17.0.3+7", f"{mcdir}/java")
    onlinemode = input("Do you want to make this server cracked? > y/n")
    if onlinemode == "y":
        print("Setting onlinemode to false...")
        open(f"{mcdir}/server.properties", 'wb').write(requests.get(
            "https://raw.githubusercontent.com/antekmeco/mcsetup/main/server.properties").content)
    open(f"{mcdir}/start.sh", 'wb').write(requests.get(
        "https://raw.githubusercontent.com/antekmeco/mcsetup/main/start.sh").content)
    os.system("clear")
    print("Everything done!!!")
    print("To start the server run ")


if __name__ == "__main__":
    main()
